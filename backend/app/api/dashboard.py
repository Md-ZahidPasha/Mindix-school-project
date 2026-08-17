from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import func, text
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.models.class_model import Class
from app.models.department import Department
from app.models.employee import Employee
from app.models.institution import Institution
from app.models.parent import Parent
from app.models.student import Student
from app.models.leave_application import LeaveApplication
from app.models.certificate import Certificate
from app.models.library_book import LibraryBook
from app.models.library_transaction import LibraryTransaction

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)
security = HTTPBearer()


@router.get("")
def get_dashboard(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    payload = decode_access_token(credentials.credentials)
    if not payload or not payload.get("institution_id"):
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token.")
    institution_id = payload["institution_id"]
    institution = db.query(Institution).filter(Institution.id == institution_id).first()
    count = lambda model: db.query(func.count(model.id)).filter(model.institution_id == institution_id).scalar() or 0

    pending_leaves = db.query(func.count(LeaveApplication.id)).filter(
        LeaveApplication.institution_id == institution_id,
        LeaveApplication.status.in_(["Pending", "pending"]),
    ).scalar() or 0

    pending_certificates = db.query(func.count(Certificate.id)).filter(
        Certificate.institution_id == institution_id,
        Certificate.status == "pending",
    ).scalar() or 0

    pending_documents = db.execute(
        text("SELECT COUNT(*) FROM documents WHERE institution_id = :iid AND status IN ('pending','PENDING','extracted')"),
        {"iid": institution_id},
    ).scalar() or 0

    timetable_conflicts = db.execute(
        text(
            "SELECT COUNT(*) FROM ("
            "SELECT class_id, day, period, COUNT(*) c FROM schedule_entries "
            "WHERE institution_id = :iid GROUP BY class_id, day, period HAVING COUNT(*) > 1"
            ") t"
        ),
        {"iid": institution_id},
    ).scalar() or 0

    total_books = db.query(func.count(LibraryBook.id)).filter(
        LibraryBook.institution_id == institution_id
    ).scalar() or 0

    issued_books = db.query(func.count(LibraryTransaction.id)).filter(
        LibraryTransaction.institution_id == institution_id,
        LibraryTransaction.status.in_(["issued", "borrowed"]),
    ).scalar() or 0

    overdue_books = db.execute(
        text(
            "SELECT COUNT(*) FROM library_transactions "
            "WHERE institution_id = :iid AND status IN ('issued','borrowed') AND due_date < CURRENT_DATE"
        ),
        {"iid": institution_id},
    ).scalar() or 0

    return {
        "institution_name": institution.institution_name if institution else "Your institution",
        "students": count(Student),
        "teachers": count(Employee),
        "parents": count(Parent),
        "classes": count(Class),
        "departments": count(Department),
        "pending_leave_requests": pending_leaves,
        "pending_certificates": pending_certificates,
        "pending_documents": pending_documents,
        "timetable_conflicts": timetable_conflicts,
        "library": {
            "total_books": total_books,
            "issued_books": issued_books,
            "overdue_books": overdue_books,
        },
        "alerts": [
            {"type": "leave", "message": "Leave request awaiting approval", "count": pending_leaves},
            {"type": "certificate", "message": "Certificate request awaiting approval", "count": pending_certificates},
            {"type": "document", "message": "Document awaiting review", "count": pending_documents},
            {"type": "timetable", "message": "Timetable conflict detected", "count": timetable_conflicts},
            {"type": "library", "message": "Overdue library books", "count": overdue_books},
        ],
    }
