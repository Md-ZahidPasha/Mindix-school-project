"""Small, deployable OpenCV face-enrollment and matching service.

This uses Haar face detection plus normalized face histograms. It is a genuine
computer-vision similarity workflow, intentionally conservative: no detected
face or low-confidence match is never marked as attendance.
"""
import json
import os
import tempfile

import cv2
import numpy as np
from sqlalchemy import text


def _load_cascade():
    """Load the Haar cascade from an ASCII-only path.

    OpenCV's C++ file loader uses the ANSI codepage on Windows, so cascades
    located under non-ASCII paths (for example a home directory containing
    non-Latin characters) fail to open. Copying the cascade XML to the system
    temp directory makes detection reliable across machines.
    """
    source = os.path.join(
        cv2.data.haarcascades, "haarcascade_frontalface_default.xml"
    )
    destination = os.path.join(
        tempfile.gettempdir(), "pb_haarcascade_frontalface_default.xml"
    )
    try:
        with open(source, "rb") as handle:
            data = handle.read()
        if os.path.exists(destination):
            with open(destination, "rb") as handle:
                if handle.read() == data:
                    return cv2.CascadeClassifier(destination)
        with open(destination, "wb") as handle:
            handle.write(data)
    except OSError:
        return cv2.CascadeClassifier(source)
    return cv2.CascadeClassifier(destination)


_CASCADE = _load_cascade()


def face_embedding(image_bytes: bytes) -> list[float]:
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("The uploaded file is not a readable image.")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = _CASCADE.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(70, 70))
    if len(faces) != 1:
        raise ValueError("Exactly one clear front-facing face is required.")
    x, y, width, height = max(faces, key=lambda item: item[2] * item[3])
    face = cv2.resize(gray[y:y + height, x:x + width], (160, 160))
    face = cv2.equalizeHist(face)
    histogram = cv2.calcHist([face], [0], None, [64], [0, 256]).flatten()
    histogram /= max(float(histogram.sum()), 1.0)
    return histogram.astype(float).tolist()


def save_face_profile(db, student_id, institution_id, embedding: list[float]):
    db.execute(text("""
        INSERT INTO student_face_profiles (student_id, institution_id, embedding, updated_at)
        VALUES (:student_id, :institution_id, CAST(:embedding AS jsonb), NOW())
        ON CONFLICT (student_id) DO UPDATE SET
            institution_id = EXCLUDED.institution_id,
            embedding = EXCLUDED.embedding,
            updated_at = NOW()
    """), {"student_id": str(student_id), "institution_id": str(institution_id), "embedding": json.dumps(embedding)})
    db.commit()


def find_face_match(db, institution_id, embedding: list[float], threshold: float = 0.88):
    rows = db.execute(text("""
        SELECT p.student_id, u.full_name, p.embedding
        FROM student_face_profiles p
        JOIN students s ON s.id = p.student_id
        JOIN users u ON u.id = s.user_id
        WHERE p.institution_id = :institution_id
    """), {"institution_id": str(institution_id)}).mappings().all()
    if not rows:
        raise ValueError("No enrolled face profiles exist for this institution.")
    probe = np.array(embedding, dtype=np.float32)
    best = None
    for row in rows:
        stored = row["embedding"]
        if isinstance(stored, str):
            stored = json.loads(stored)
        candidate = np.array(stored, dtype=np.float32)
        score = float(cv2.compareHist(probe, candidate, cv2.HISTCMP_CORREL))
        if best is None or score > best["confidence"]:
            best = {"student_id": row["student_id"], "full_name": row["full_name"], "confidence": score}
    if best is None or best["confidence"] < threshold:
        raise ValueError("Face could not be verified with sufficient confidence.")
    return best
