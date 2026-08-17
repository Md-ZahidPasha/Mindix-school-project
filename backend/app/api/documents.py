import json
from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import decode_access_token

from app.services.document_service import (
    extract_document,
    save_verified_document,
)


router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"],
)
security = HTTPBearer()


def require_authenticated_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token.")
    return user


# ============================================================
# AI DOCUMENT EXTRACTION
# ============================================================

@router.post("/extract")
async def extract_document_api(
    file: UploadFile = File(...),
    current_user: dict = Depends(require_authenticated_user),
):
    try:
        file_bytes = await file.read()

        if not file_bytes:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty.",
            )

        mime_type = (
            file.content_type
            or "application/octet-stream"
        )

        extracted_data = extract_document(
            file_bytes,
            mime_type,
            file.filename or "unknown",
        )

        return {
            "status": "success",
            "message": "Document processed successfully",
            "filename": file.filename,
            "data": extracted_data.model_dump(
                mode="json"
            ),
        }

    except HTTPException:
        raise

    except Exception as e:
        print(
            "Document extraction error:",
            repr(e),
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to process document.",
        )


# ============================================================
# ADMIN VERIFY & SAVE
# ============================================================

@router.post("/save")
async def save_document(
    file: UploadFile = File(...),
    institution_id: UUID = Form(...),
    document_type: str = Form(...),
    data: str = Form(...),
    confidence: float | None = Form(default=None),
    uploaded_by: UUID | None = Form(default=None),
    reviewed_by: UUID | None = Form(default=None),
    current_user: dict = Depends(require_authenticated_user),
):
    try:
        # ----------------------------------------------------
        # 1. Read uploaded document
        # ----------------------------------------------------

        file_bytes = await file.read()

        if not file_bytes:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty.",
            )

        # ----------------------------------------------------
        # 2. Parse dynamic JSON
        # ----------------------------------------------------

        try:
            extracted_data = json.loads(data)

        except json.JSONDecodeError:
            raise HTTPException(
                status_code=400,
                detail="Invalid JSON in 'data' field.",
            )

        if not isinstance(extracted_data, dict):
            raise HTTPException(
                status_code=400,
                detail="'data' must be a JSON object.",
            )

        # ----------------------------------------------------
        # 3. Support both:
        #
        # A) Correct frontend format:
        #
        # {
        #   "institution_name": "...",
        #   "full_name": "..."
        # }
        #
        # B) Full /extract response accidentally sent:
        #
        # {
        #   "status": "success",
        #   "message": "...",
        #   "filename": "...",
        #   "data": {
        #       "document_type": "...",
        #       "confidence": 0.99,
        #       "data": {
        #           ...
        #       }
        #   }
        # }
        # ----------------------------------------------------

        if (
            "status" in extracted_data
            and "data" in extracted_data
            and isinstance(
                extracted_data["data"],
                dict,
            )
        ):
            extraction_wrapper = extracted_data["data"]

            if (
                "data" in extraction_wrapper
                and isinstance(
                    extraction_wrapper["data"],
                    dict,
                )
            ):
                extracted_data = (
                    extraction_wrapper["data"]
                )

            else:
                extracted_data = extraction_wrapper

        # ----------------------------------------------------
        # 4. Confidence validation
        # ----------------------------------------------------

        if confidence is not None:
            if not 0 <= confidence <= 1:
                raise HTTPException(
                    status_code=400,
                    detail=(
                        "Confidence must be between 0 and 1."
                    ),
                )

        # ----------------------------------------------------
        # 5. MIME type
        # ----------------------------------------------------

        mime_type = (
            file.content_type
            or "application/octet-stream"
        )

        # ----------------------------------------------------
        # 6. Upload to Storage + save to documents table
        # ----------------------------------------------------

        saved_document = save_verified_document(
            file_bytes=file_bytes,
            filename=file.filename or "unknown",
            mime_type=mime_type,
            institution_id=institution_id,
            uploaded_by=uploaded_by,
            reviewed_by=reviewed_by,
            document_type=document_type,
            confidence=confidence,
            extracted_data=extracted_data,
        )

        # ----------------------------------------------------
        # 7. Success response
        # ----------------------------------------------------

        return {
            "status": "success",
            "message": (
                "Document verified and saved successfully."
            ),
            "data": saved_document,
        }

    except HTTPException:
        raise

    except Exception as e:
        print(
            "Document save error:",
            repr(e),
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to save document.",
        )
