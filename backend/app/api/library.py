from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.models.student import Student
from app.schemas.library import (
    BookCreate,
    BookResponse,
    BookUpdate,
    BorrowRequest,
    LibraryStats,
    ReturnRequest,
    TransactionResponse,
)
from app.services.library_service import (
    borrow_book,
    borrowed_books,
    create_book,
    delete_book,
    get_book,
    history,
    library_stats,
    list_books,
    overdue_books,
    return_book,
    update_book,
)

router = APIRouter(prefix="/api/library", tags=["Digital Library"])
security = HTTPBearer()

STAFF_ROLES = {"admin", "principal", "teacher", "staff"}


def _get_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token.")
    if not user.get("institution_id"):
        raise HTTPException(status_code=401, detail="Token is missing the institution scope.")
    return user


def _require_staff(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    user = _get_user(credentials)
    if (user.get("role") or "").lower() not in STAFF_ROLES:
        raise HTTPException(status_code=403, detail="Staff authorization is required.")
    return user


# ==========================================
# Books CRUD
# ==========================================
@router.get("/books", response_model=list[BookResponse])
def list_books_endpoint(
    search: str | None = Query(default=None),
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    return list_books(db, UUID(user["institution_id"]), search=search)


@router.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book_endpoint(
    data: BookCreate,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    try:
        return create_book(db, UUID(user["institution_id"]), data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="A book with this ISBN already exists.")


@router.get("/books/{book_id}", response_model=BookResponse)
def get_book_endpoint(
    book_id: UUID,
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    book = get_book(db, UUID(user["institution_id"]), book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


@router.put("/books/{book_id}", response_model=BookResponse)
def update_book_endpoint(
    book_id: UUID,
    data: BookUpdate,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    book = update_book(db, UUID(user["institution_id"]), book_id, data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


@router.delete("/books/{book_id}")
def delete_book_endpoint(
    book_id: UUID,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    book = delete_book(db, UUID(user["institution_id"]), book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return {"status": "success", "message": "Book deleted."}


# ==========================================
# Borrowing
# ==========================================
@router.post("/borrow", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def borrow_endpoint(
    data: BorrowRequest,
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    role = (user.get("role") or "").lower()
    student_id = data.student_id
    if role == "student":
        student = (
            db.query(Student)
            .filter(
                Student.student_id == user.get("student_id"),
                Student.institution_id == user.get("institution_id"),
            )
            .first()
        )
        if not student:
            raise HTTPException(status_code=403, detail="Student scope is missing from the token.")
        student_id = student.id
    elif role not in STAFF_ROLES:
        raise HTTPException(status_code=403, detail="A student scope is required to borrow.")
    try:
        return borrow_book(db, UUID(user["institution_id"]), student_id, data.book_id, data.due_date)
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))


@router.post("/return", response_model=TransactionResponse)
def return_endpoint(
    data: ReturnRequest,
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    try:
        return return_book(db, UUID(user["institution_id"]), data.transaction_id)
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))


# ==========================================
# Records
# ==========================================
@router.get("/borrowed", response_model=list[TransactionResponse])
def borrowed_endpoint(
    student_id: UUID | None = Query(default=None),
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    role = (user.get("role") or "").lower()
    if role == "student":
        student = (
            db.query(Student)
            .filter(
                Student.student_id == user.get("student_id"),
                Student.institution_id == user.get("institution_id"),
            )
            .first()
        )
        if not student:
            raise HTTPException(status_code=403, detail="Student scope is missing from the token.")
        student_id = student.id
    return borrowed_books(db, UUID(user["institution_id"]), student_id)


@router.get("/history", response_model=list[TransactionResponse])
def history_endpoint(
    student_id: UUID | None = Query(default=None),
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    role = (user.get("role") or "").lower()
    if role == "student":
        student = (
            db.query(Student)
            .filter(
                Student.student_id == user.get("student_id"),
                Student.institution_id == user.get("institution_id"),
            )
            .first()
        )
        if not student:
            raise HTTPException(status_code=403, detail="Student scope is missing from the token.")
        student_id = student.id
    return history(db, UUID(user["institution_id"]), student_id)


@router.get("/overdue", response_model=list[TransactionResponse])
def overdue_endpoint(
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    return overdue_books(db, UUID(user["institution_id"]))


@router.get("/stats", response_model=LibraryStats)
def stats_endpoint(
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    return library_stats(db, UUID(user["institution_id"]))