from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import decode_access_token
from app.schemas.ai import AIChatRequest, AIChatResponse
from app.services.ai_service import generate_ai_response


router = APIRouter(
    prefix="/api/ai",
    tags=["AI Assistant"],
)


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired authentication token.",
        )

    return payload


@router.post(
    "/chat",
    response_model=AIChatResponse,
)
def ai_chat(
    request: AIChatRequest,
    current_user: dict = Depends(get_current_user),
):
    role = current_user.get("role")
    institution_id = current_user.get("institution_id")

    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty.",
        )

    try:
        answer = generate_ai_response(
            message=request.message,
            role=role,
            institution_id=institution_id,
        )

        return AIChatResponse(
            status="success",
            answer=answer,
            role=role,
            institution_id=institution_id,
        )

    except Exception as e:
        print("AI Assistant error:", e)

        raise HTTPException(
            status_code=500,
            detail="Failed to process AI Assistant request.",
        )