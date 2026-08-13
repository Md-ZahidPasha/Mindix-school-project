import json
import os
import uuid
from datetime import datetime, timezone
from urllib.parse import quote

import httpx
from google import genai
from supabase import create_client

from app.core.config import settings
from app.schemas.document import DocumentExtractionResponse


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


# ============================================================
# AI DOCUMENT EXTRACTION
# ============================================================

def extract_document(
    file_bytes: bytes,
    mime_type: str,
    filename: str,
) -> DocumentExtractionResponse:

    prompt = """
You are PaperBuddy AI, an intelligent document processing system
for schools, colleges and educational institutions.

Analyze the uploaded document carefully.

Your job is to:

1. Identify what type of document this is.
2. Read all useful information from the document.
3. Extract the important fields and values.
4. Work with school/institution documents such as:
   - admission forms
   - student applications
   - marksheets
   - certificates
   - bonafide applications
   - transfer certificates
   - birth certificates
   - ID documents
   - teacher documents
   - staff documents
   - principal documents
   - qualification certificates
   - experience certificates
   - attendance documents
   - fee documents
   - examination documents
   - scholarship forms
   - leave applications
   - institutional documents
   - and other educational documents.

Rules:

- Do NOT invent information.
- If a field is not present, do not create it.
- Preserve the actual values found in the document.
- Extract names, dates, IDs, phone numbers, emails, addresses,
  qualifications, marks, subjects, classes, courses,
  institution names and other relevant information.
- If the document contains a table, preserve the table information.
- If the document is a certificate, identify the certificate type
  and extract its important details.
- If the document is an application, identify the purpose of
  the application and extract the applicant's information.
- If the document is an image or scanned paper, use visual
  understanding to read it.
- If handwriting is present and readable, extract it.
- Do not guess unclear handwriting or unreadable information.
- Keep numbers, dates, IDs and names exactly as they appear
  whenever possible.
- The fields inside "data" must depend on the actual document.
- Do not force every document into the same set of fields.
- Return valid JSON only.

The JSON response MUST have exactly this structure:

{
    "document_type": "type of document",
    "confidence": 0.0,
    "data": {
        "field_name": "extracted value"
    }
}

The confidence value must be between 0 and 1.

The "data" object can contain any relevant fields found in
the document.

If a piece of information is missing, do not add it.

Filename:
""" + filename

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=[
                prompt,
                {
                    "inline_data": {
                        "mime_type": mime_type,
                        "data": file_bytes,
                    },
                },
            ],
            config={
                "response_mime_type": "application/json",
            },
        )

        data = json.loads(response.text)

        return DocumentExtractionResponse.model_validate(data)

    except Exception as e:
        print("Gemini extraction error:", repr(e))
        raise


# ============================================================
# SUPABASE CLIENT
# ============================================================

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SERVICE_ROLE_KEY,
)


# ============================================================
# SUPABASE STORAGE REST UPLOAD
# ============================================================

def _upload_to_supabase_storage(
    storage_path: str,
    file_bytes: bytes,
    mime_type: str,
) -> None:
    """
    Upload a file directly to Supabase Storage using the
    Storage REST API.

    This avoids the Storage3 client response-parsing issue
    encountered with the current environment.
    """

    bucket_name = "school-documents"

    storage_url = (
        f"{settings.SUPABASE_URL.rstrip('/')}"
        f"/storage/v1/object/"
        f"{quote(bucket_name, safe='')}/"
        f"{quote(storage_path, safe='/')}"
    )

    headers = {
        "Authorization": (
            f"Bearer {settings.SUPABASE_SERVICE_ROLE_KEY}"
        ),
        "apikey": settings.SUPABASE_SERVICE_ROLE_KEY,
        "Content-Type": mime_type,
        "x-upsert": "false",
    }

    with httpx.Client(timeout=60.0) as http_client:
        response = http_client.post(
            storage_url,
            content=file_bytes,
            headers=headers,
        )

    if response.status_code >= 400:
        try:
            error_body = response.json()
        except Exception:
            error_body = response.text

        raise RuntimeError(
            f"Supabase Storage upload failed "
            f"({response.status_code}): {error_body}"
        )


# ============================================================
# SUPABASE STORAGE DELETE
# ============================================================

def _delete_from_supabase_storage(
    storage_path: str,
) -> None:
    """
    Delete an uploaded file from Supabase Storage.
    Used only when database insertion fails.
    """

    bucket_name = "school-documents"

    storage_url = (
        f"{settings.SUPABASE_URL.rstrip('/')}"
        f"/storage/v1/object/"
        f"{quote(bucket_name, safe='')}/"
        f"{quote(storage_path, safe='/')}"
    )

    headers = {
        "Authorization": (
            f"Bearer {settings.SUPABASE_SERVICE_ROLE_KEY}"
        ),
        "apikey": settings.SUPABASE_SERVICE_ROLE_KEY,
    }

    with httpx.Client(timeout=30.0) as http_client:
        response = http_client.delete(
            storage_url,
            headers=headers,
        )

    if response.status_code >= 400:
        print(
            "Supabase Storage cleanup failed:",
            response.status_code,
            response.text,
        )


# ============================================================
# SAVE VERIFIED DOCUMENT
# ============================================================

def save_verified_document(
    file_bytes: bytes,
    filename: str,
    mime_type: str,
    institution_id,
    uploaded_by,
    reviewed_by,
    document_type: str,
    confidence: float | None,
    extracted_data: dict,
):
    """
    Upload the verified document to Supabase Storage
    and save its metadata/extracted data in public.documents.
    """

    document_id = uuid.uuid4()

    # Prevent directory/path traversal.
    safe_filename = os.path.basename(filename)

    storage_path = (
        f"institutions/"
        f"{institution_id}/"
        f"documents/"
        f"{document_id}/"
        f"{safe_filename}"
    )

    storage_uploaded = False

    try:

        # ----------------------------------------------------
        # 1. Upload original document
        # ----------------------------------------------------

        _upload_to_supabase_storage(
            storage_path=storage_path,
            file_bytes=file_bytes,
            mime_type=mime_type,
        )

        storage_uploaded = True

        print(
            "Document uploaded to Storage:",
            storage_path,
        )

        # ----------------------------------------------------
        # 2. Prepare database record
        # ----------------------------------------------------

        now = datetime.now(timezone.utc).isoformat()

        document_record = {
            "id": str(document_id),
            "institution_id": str(institution_id),

            "uploaded_by": (
                str(uploaded_by)
                if uploaded_by
                else None
            ),

            "filename": safe_filename,
            "document_type": document_type,
            "mime_type": mime_type,
            "file_path": storage_path,
            "confidence": confidence,

            "extracted_data": extracted_data,

            "status": "verified",

            "reviewed_by": (
                str(reviewed_by)
                if reviewed_by
                else None
            ),

            "reviewed_at": now,
        }

        # ----------------------------------------------------
        # 3. Insert into public.documents
        # ----------------------------------------------------

        response = (
            supabase
            .table("documents")
            .insert(document_record)
            .execute()
        )

        if not response.data:
            raise RuntimeError(
                "Document was uploaded to Storage, "
                "but database insertion returned no data."
            )

        print(
            "Document saved in public.documents:",
            document_id,
        )

        return response.data[0]

    except Exception as e:

        print(
            "Document save error:",
            repr(e),
        )

        # ----------------------------------------------------
        # 4. Cleanup Storage if DB insertion failed
        # ----------------------------------------------------

        if storage_uploaded:
            try:
                _delete_from_supabase_storage(
                    storage_path
                )
            except Exception as cleanup_error:
                print(
                    "Storage cleanup error:",
                    repr(cleanup_error),
                )

        raise