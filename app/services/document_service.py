from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.document import Document

def get_document_or_404(document_id: int, db: Session) -> Document:
    document = db.query(Document).filter(Document.id == document_id).first()

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return document