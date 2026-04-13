from fastapi import FastAPI
from app.api import documents

app = FastAPI()

app.include_router(documents.router)

@app.get("/")
def root():
    return {"message": "API is running "}