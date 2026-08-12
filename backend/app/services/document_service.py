import json
import os

from google import genai

from app.schemas.document import DocumentExtractionResponse


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


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