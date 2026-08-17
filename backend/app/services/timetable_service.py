from ortools.sat.python import cp_model

from app.schemas.timetable import (
    TimetableGenerateRequest,
    TimetableSlotResponse,
    TimetableLesson,
)


def solve_timetable(
    lessons: list[TimetableLesson],
    working_days: list[str],
    periods_per_day: int,
) -> list[TimetableSlotResponse]:
    """Generate a conflict-free timetable with CP-SAT.

    Hard constraints (each enforced per time slot):
    - a teacher teaches at most one lesson,
    - a class has at most one lesson,
    - a room hosts at most one lesson (only enforced for lessons that are
      actually assigned a room, so classes without a room are not over-constrained).
    """
    model = cp_model.CpModel()
    positions = [
        (day_index, period)
        for day_index in range(len(working_days))
        for period in range(1, periods_per_day + 1)
    ]
    occurrences = [
        lesson
        for lesson in lessons
        for _ in range(lesson.sessions_per_week)
    ]
    choices = [
        [model.NewBoolVar(f"lesson_{i}_at_{p}") for p in range(len(positions))]
        for i in range(len(occurrences))
    ]
    for lesson_choices in choices:
        model.AddExactlyOne(lesson_choices)

    for position_index in range(len(positions)):
        for attribute in ("teacher_id", "class_id"):
            groups: dict[str, list[int]] = {}
            for index, lesson in enumerate(occurrences):
                groups.setdefault(getattr(lesson, attribute), []).append(index)
            for indexes in groups.values():
                model.Add(sum(choices[i][position_index] for i in indexes) <= 1)
        # Room constraint: only lessons that were assigned a real room compete.
        room_groups: dict[str, list[int]] = {}
        for index, lesson in enumerate(occurrences):
            if lesson.room.strip():
                room_groups.setdefault(lesson.room, []).append(index)
        for indexes in room_groups.values():
            model.Add(sum(choices[i][position_index] for i in indexes) <= 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 8
    if solver.Solve(model) not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise ValueError("No conflict-free timetable can be generated with these constraints.")

    result = []
    for index, lesson in enumerate(occurrences):
        position_index = next(
            p for p in range(len(positions)) if solver.Value(choices[index][p])
        )
        day_index, period = positions[position_index]
        result.append(
            TimetableSlotResponse(
                day=working_days[day_index],
                period=period,
                **lesson.model_dump(exclude={"sessions_per_week"}),
            )
        )
    return sorted(
        result,
        key=lambda slot: (working_days.index(slot.day), slot.period, slot.class_name),
    )


def generate_timetable(request: TimetableGenerateRequest) -> list[TimetableSlotResponse]:
    """Generate a timetable from a client-supplied lesson list."""
    return solve_timetable(request.lessons, request.working_days, request.periods_per_day)