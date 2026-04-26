from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
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

@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    text = content.decode("utf-8")

    db_document = Document(
        title=file.filename,
        content=text,
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return {
        "id": db_document.id,
        "filename": file.filename,
        "message": "Document uploaded successfully"
    }

@router.get("/documents/{document_id}", response_model=DocumentRead)
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return document