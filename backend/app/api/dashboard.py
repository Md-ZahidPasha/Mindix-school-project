from fastapi import APIRouter

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def get_dashboard():
    return {
        "institution_name": "aloi institute",
        "students": 0,
        "teachers": 0,
        "parents": 0,
        "classes": 0,
        "departments": 0
    }