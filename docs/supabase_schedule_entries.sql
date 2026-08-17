-- Safe additive migration for PaperBuddy schedule / timetable.
-- Run once against the EXISTING Supabase Postgres database. It creates only the
-- new schedule_entries table and its indexes; it does not modify or delete any
-- existing table or record.
--
-- The unique indexes below are the database-level guarantee that one class,
-- teacher or room is never booked twice in the same day + period.

CREATE TABLE IF NOT EXISTS public.schedule_entries (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    institution_id uuid NOT NULL REFERENCES public.institutions(id) ON DELETE CASCADE,
    class_id uuid NOT NULL REFERENCES public.classes(id) ON DELETE CASCADE,
    section varchar(255),
    subject_id uuid REFERENCES public.subjects(id) ON DELETE CASCADE,
    subject_name varchar(255) NOT NULL,
    teacher_id uuid REFERENCES public.teachers(id) ON DELETE SET NULL,
    teacher_name varchar(255),
    room_id uuid REFERENCES public.rooms(id) ON DELETE SET NULL,
    room_name varchar(255),
    day varchar(50) NOT NULL,
    period integer NOT NULL,
    source varchar(20) NOT NULL DEFAULT 'manual',
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_schedule_entries_institution
    ON public.schedule_entries (institution_id);
CREATE INDEX IF NOT EXISTS idx_schedule_entries_class
    ON public.schedule_entries (class_id);
CREATE INDEX IF NOT EXISTS idx_schedule_entries_teacher
    ON public.schedule_entries (teacher_id);

-- A class must have at most one lesson per day + period.
CREATE UNIQUE INDEX IF NOT EXISTS uq_schedule_entries_class_slot
    ON public.schedule_entries (class_id, day, period);

-- A teacher must have at most one lesson per day + period.
CREATE UNIQUE INDEX IF NOT EXISTS uq_schedule_entries_teacher_slot
    ON public.schedule_entries (teacher_id, day, period)
    WHERE teacher_id IS NOT NULL;

-- A room must host at most one lesson per day + period.
CREATE UNIQUE INDEX IF NOT EXISTS uq_schedule_entries_room_slot
    ON public.schedule_entries (room_id, day, period)
    WHERE room_id IS NOT NULL;