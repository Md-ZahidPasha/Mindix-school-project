from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
)

from app.services.task_service import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task,
)


router = APIRouter(
    prefix="/api/tasks",
    tags=["Tasks"],
)


# ==========================================
# Create Task
# ==========================================
@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task_endpoint(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
):
    return create_task(
        db,
        task_data,
    )


# ==========================================
# List Tasks
# ==========================================
@router.get(
    "",
    response_model=list[TaskResponse],
)
def list_tasks(
    institution_id: UUID,
    employee_id: UUID | None = None,
    db: Session = Depends(get_db),
):
    return get_tasks(
        db,
        institution_id,
        employee_id,
    )


# ==========================================
# Get One Task
# ==========================================
@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
def get_task_endpoint(
    task_id: UUID,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    task = get_task(
        db,
        task_id,
        institution_id,
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


# ==========================================
# Update Task
# ==========================================
@router.put(
    "/{task_id}",
    response_model=TaskResponse,
)
def update_task_endpoint(
    task_id: UUID,
    task_data: TaskUpdate,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    task = update_task(
        db,
        task_id,
        institution_id,
        task_data,
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


# ==========================================
# Delete Task
# ==========================================
@router.delete(
    "/{task_id}",
)
def delete_task_endpoint(
    task_id: UUID,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    deleted = delete_task(
        db,
        task_id,
        institution_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return {
        "status": "success",
        "message": "Task deleted successfully",
    }