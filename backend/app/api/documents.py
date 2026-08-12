from typing import Any

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel

from app.services.document_service import extract_document


router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"],
)


# ============================================================
# ADMIN REVIEW / SAVE REQUEST
# ============================================================

class DocumentSaveRequest(BaseModel):
    filename: str
    document_type: str
    confidence: float | None = None
    data: dict[str, Any]


# ============================================================
# AI DOCUMENT EXTRACTION
# ============================================================

@router.post("/extract")
async def extract_document_api(
    file: UploadFile = File(...)
):
    try:
        file_bytes = await file.read()

        if not file_bytes:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        # Use the MIME type provided by the browser.
        mime_type = file.content_type or "application/octet-stream"

        extracted_data = extract_document(
            file_bytes,
            mime_type,
            file.filename or "unknown"
        )

        return {
            "status": "success",
            "message": "Document processed successfully",
            "filename": file.filename,
            "data": extracted_data.model_dump(mode="json"),
        }

    except HTTPException:
        raise

    except Exception as e:
        print("Document extraction error:", e)

        raise HTTPException(
            status_code=500,
            detail="Failed to process document."
        )


# ============================================================
# ADMIN VERIFY & SAVE
# ============================================================

@router.post("/save")
async def save_document(
    request: DocumentSaveRequest
):
    try:
        # ----------------------------------------------------
        # TEMPORARY SAVE
        #
        # Supabase database insertion will be connected after
        # Haseeb creates the documents table.
        # ----------------------------------------------------

        verified_document = {
            "filename": request.filename,
            "document_type": request.document_type,
            "confidence": request.confidence,
            "data": request.data,
            "status": "verified",
        }

        print("Verified document:")
        print(verified_document)

        return {
            "status": "success",
            "message": "Document verified successfully.",
            "data": verified_document,
        }

    except Exception as e:
        print("Document save error:", e)

        raise HTTPException(
            status_code=500,
            detail="Failed to save document."
        )