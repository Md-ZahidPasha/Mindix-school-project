from datetime import date, timedelta
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.models.library_book import LibraryBook
from app.models.library_transaction import LibraryTransaction
from app.schemas.library import BookCreate, BookUpdate

LOAN_DAYS = 14
FINE_PER_DAY = 5.0


def _book_to_dict(b: LibraryBook) -> dict:
    return {
        "id": b.id,
        "institution_id": b.institution_id,
        "title": b.title,
        "author": b.author,
        "isbn": b.isbn,
        "total_copies": b.total_copies,
        "available_copies": b.available_copies,
        "created_at": b.created_at,
    }


def create_book(db: Session, institution_id: UUID, data: BookCreate):
    book = LibraryBook(
        institution_id=institution_id,
        title=data.title,
        author=data.author,
        isbn=data.isbn,
        total_copies=data.total_copies,
        available_copies=data.available_copies
        if data.available_copies is not None
        else data.total_copies,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return _book_to_dict(book)


def list_books(db: Session, institution_id: UUID, search: str | None = None):
    query = db.query(LibraryBook).filter(LibraryBook.institution_id == institution_id)
    if search:
        like = f"%{search}%"
        query = query.filter(
            LibraryBook.title.ilike(like) | LibraryBook.author.ilike(like) | LibraryBook.isbn.ilike(like)
        )
    return [_book_to_dict(b) for b in query.order_by(LibraryBook.title).all()]


def get_book(db: Session, institution_id: UUID, book_id: UUID):
    return (
        db.query(LibraryBook)
        .filter(LibraryBook.id == book_id, LibraryBook.institution_id == institution_id)
        .first()
    )


def update_book(db: Session, institution_id: UUID, book_id: UUID, data: BookUpdate):
    book = get_book(db, institution_id, book_id)
    if not book:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return _book_to_dict(book)


def delete_book(db: Session, institution_id: UUID, book_id: UUID):
    book = get_book(db, institution_id, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book


def _transaction_to_dict(db: Session, institution_id: UUID, t: LibraryTransaction) -> dict:
    fine = None
    days_overdue = None
    if t.status == "issued" and t.due_date and t.due_date < date.today():
        days_overdue = (date.today() - t.due_date).days
        fine = round(days_overdue * FINE_PER_DAY, 2)

    book = (
        db.query(LibraryBook).filter(LibraryBook.id == t.book_id).first()
    )
    student_row = db.execute(
        text("SELECT s.roll_number, u.full_name FROM students s LEFT JOIN users u ON u.id = s.user_id WHERE s.id = :sid"),
        {"sid": str(t.student_id)},
    ).mappings().first()

    return {
        "id": t.id,
        "student_id": t.student_id,
        "book_id": t.book_id,
        "institution_id": t.institution_id,
        "issue_date": t.issue_date,
        "due_date": t.due_date,
        "return_date": t.return_date,
        "status": t.status,
        "created_at": t.created_at,
        "book_title": book.title if book else None,
        "book_author": book.author if book else None,
        "student_name": student_row["full_name"] if student_row else None,
        "student_roll": student_row["roll_number"] if student_row else None,
        "fine": fine,
        "days_overdue": days_overdue,
    }


def borrow_book(db: Session, institution_id: UUID, student_id: UUID, book_id: UUID, due_date: date | None = None):
    book = get_book(db, institution_id, book_id)
    if not book:
        raise ValueError("Book not found in this institution.")
    if not book.available_copies or book.available_copies <= 0:
        raise ValueError("Book is not available. All copies are issued.")

    already = (
        db.query(LibraryTransaction)
        .filter(
            LibraryTransaction.book_id == book_id,
            LibraryTransaction.student_id == student_id,
            LibraryTransaction.status == "issued",
        )
        .first()
    )
    if already:
        raise ValueError("You have already borrowed this book.")

    book.available_copies -= 1
    transaction = LibraryTransaction(
        student_id=student_id,
        book_id=book_id,
        institution_id=institution_id,
        issue_date=date.today(),
        due_date=due_date or (date.today() + timedelta(days=LOAN_DAYS)),
        status="issued",
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return _transaction_to_dict(db, institution_id, transaction)


def return_book(db: Session, institution_id: UUID, transaction_id: UUID):
    t = (
        db.query(LibraryTransaction)
        .filter(LibraryTransaction.id == transaction_id, LibraryTransaction.institution_id == institution_id)
        .first()
    )
    if not t:
        raise ValueError("Transaction not found.")
    if t.status == "returned":
        raise ValueError("Book has already been returned.")
    book = get_book(db, institution_id, t.book_id)
    if book:
        book.available_copies = min(book.total_copies, (book.available_copies or 0) + 1)
    t.status = "returned"
    t.return_date = date.today()
    db.commit()
    db.refresh(t)
    return _transaction_to_dict(db, institution_id, t)


def borrowed_books(db: Session, institution_id: UUID, student_id: UUID | None = None):
    query = db.query(LibraryTransaction).filter(
        LibraryTransaction.institution_id == institution_id,
        LibraryTransaction.status == "issued",
    )
    if student_id:
        query = query.filter(LibraryTransaction.student_id == student_id)
    return [_transaction_to_dict(db, institution_id, t) for t in query.order_by(LibraryTransaction.due_date).all()]


def history(db: Session, institution_id: UUID, student_id: UUID | None = None):
    query = db.query(LibraryTransaction).filter(LibraryTransaction.institution_id == institution_id)
    if student_id:
        query = query.filter(LibraryTransaction.student_id == student_id)
    return [_transaction_to_dict(db, institution_id, t) for t in query.order_by(LibraryTransaction.created_at.desc()).all()]


def overdue_books(db: Session, institution_id: UUID):
    return [
        t
        for t in borrowed_books(db, institution_id)
        if t["days_overdue"]
    ]


def library_stats(db: Session, institution_id: UUID):
    books = db.query(LibraryBook).filter(LibraryBook.institution_id == institution_id).all()
    borrowed = borrowed_books(db, institution_id)
    total_copies = sum((b.total_copies or 0) for b in books)
    available = sum((b.available_copies or 0) for b in books)
    active_borrowers = len({t["student_id"] for t in borrowed})
    return {
        "total_books": len(books),
        "total_copies": total_copies,
        "available_copies": available,
        "issued_books": len(borrowed),
        "overdue_books": len(overdue_books(db, institution_id)),
        "active_borrowers": active_borrowers,
    }