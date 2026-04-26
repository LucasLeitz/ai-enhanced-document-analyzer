# ai-enhanced-document-analyzer
AI-powered document analysis platform that allows users to upload files and ask questions using retrieval-augmented generation (RAG) with FastAPI, PostgreSQL, and modern React UI.


**To start the app**
1. Start up the docker container: docker compose up -d
2. Start up ollama: ollama serve
3. Start the fast-api backend: uvicorn app.main:app --reload
4. Start the React frontend:
   4a. cd frontend
   4b. npm run dev

Swagger UI (local): http://127.0.0.1:8000/docs

