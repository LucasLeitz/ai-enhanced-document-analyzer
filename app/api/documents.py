from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentResponse, DocumentRead

router = APIRouter()

@router.get("/documents", response_model=list[DocumentRead])
def list_documents(db: Session = Depends(get_db)):
    documents = db.query(Document).all()
    return documents

@router.post("/documents", response_model = DocumentResponse)
def create_document(document: DocumentCreate, db: Session = Depends(get_db)):

    db_document = Document(
        title=document.title,
        content=document.content
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return {
        "title": document.title,
        "content": document.content,
        "message": "Document created successfully"
    }