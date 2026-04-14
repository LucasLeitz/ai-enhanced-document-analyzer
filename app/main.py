from fastapi import FastAPI
from app.api import documents
from app.db.base import Base
from app.db.session import engine
from app.models.document import Document

app = FastAPI()
app.include_router(documents.router)

@app.get("/")
def root():
    return {"message": "API is running "}