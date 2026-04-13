from fastapi import APIRouter
from app.schemas.document import DocumentCreate, DocumentResponse

router = APIRouter()

@router.get("/documents")
def list_documents():
    return {"documents": []}

@router.post("/documents", response_model = DocumentResponse)
def create_document(document: DocumentCreate):
    return {
        "title": document.title,
        "content": document.content,
        "message": "Document created successfully"
    }