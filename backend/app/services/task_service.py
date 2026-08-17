from uuid import UUID

from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


# ==========================================
# Create Task
# ==========================================
def create_task(
    db: Session,
    task_data: TaskCreate,
):
    task = Task(
        **task_data.model_dump()
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


# ==========================================
# Get Tasks
# ==========================================
def get_tasks(
    db: Session,
    institution_id: UUID,
    employee_id: UUID | None = None,
):
    query = (
        db.query(Task)
        .filter(
            Task.institution_id == institution_id
        )
    )

    if employee_id:
        query = query.filter(
            Task.employee_id == employee_id
        )

    return (
        query
        .order_by(Task.created_at.desc())
        .all()
    )


# ==========================================
# Get One Task
# ==========================================
def get_task(
    db: Session,
    task_id: UUID,
    institution_id: UUID,
):
    return (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.institution_id == institution_id,
        )
        .first()
    )


# ==========================================
# Update Task
# ==========================================
def update_task(
    db: Session,
    task_id: UUID,
    institution_id: UUID,
    task_data: TaskUpdate,
):
    task = get_task(
        db,
        task_id,
        institution_id,
    )

    if not task:
        return None

    data = task_data.model_dump(
        exclude_unset=True
    )

    for field, value in data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


# ==========================================
# Delete Task
# ==========================================
def delete_task(
    db: Session,
    task_id: UUID,
    institution_id: UUID,
):
    task = get_task(
        db,
        task_id,
        institution_id,
    )

    if not task:
        return False

    db.delete(task)
    db.commit()

    return True