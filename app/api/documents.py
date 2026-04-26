from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from pypdf import PdfReader
import io

from app.db.session import get_db
from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentResponse, DocumentRead, DocumentQuestion
from app.services.ai_service import summarize_text, answer_question_about_text
from app.services.document_service import get_document_or_404

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

    if file.filename.lower().endswith((".pdf", ".PDF")):
        pdf_reader = PdfReader(io.BytesIO(content))
        text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    else:
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
    return get_document_or_404(document_id, db)

@router.post("/documents/{document_id}/summarize")
def summarize_document(document_id: int, db: Session = Depends(get_db)):
    document = get_document_or_404(document_id, db)
    summary = summarize_text(document.content)

    return {
        "document_id": document_id,
        "title": document.title,
        "summary": summary
    }

@router.post("/documents/{document_id}/ask")
def ask_document_question(
        document_id: int,
        request: DocumentQuestion,
        db: Session = Depends(get_db)
):
    document = get_document_or_404(document_id, db)

    answer = answer_question_about_text(document.content, request.question)

    return {
        "document_id": document.id,
        "title": document.title,
        "question": request.question,
        "answer": answer
    }























