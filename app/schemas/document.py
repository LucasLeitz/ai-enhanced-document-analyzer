from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title: str
    content: str

class DocumentResponse(BaseModel):
    title: str
    content: str
    message: str