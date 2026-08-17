from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str
    author: str | None = None
    isbn: str | None = None
    total_copies: int = 1
    available_copies: int | None = None


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    isbn: str | None = None
    total_copies: int | None = None
    available_copies: int | None = None


class BookResponse(BaseModel):
    id: UUID
    institution_id: UUID | None = None
    title: str
    author: str | None = None
    isbn: str | None = None
    total_copies: int | None = None
    available_copies: int | None = None
    created_at: datetime | None = None

    model_config = {"from_attributes": True}


class BorrowRequest(BaseModel):
    student_id: UUID | None = None
    book_id: UUID
    due_date: date | None = None


class ReturnRequest(BaseModel):
    transaction_id: UUID


class TransactionResponse(BaseModel):
    id: UUID
    student_id: UUID
    book_id: UUID
    institution_id: UUID | None = None
    issue_date: date | None = None
    due_date: date | None = None
    return_date: date | None = None
    status: str | None = None
    created_at: datetime | None = None
    book_title: str | None = None
    book_author: str | None = None
    student_name: str | None = None
    student_roll: str | None = None
    fine: float | None = None
    days_overdue: int | None = None

    model_config = {"from_attributes": True}


class LibraryStats(BaseModel):
    total_books: int
    total_copies: int
    available_copies: int
    issued_books: int
    overdue_books: int
    active_borrowers: int