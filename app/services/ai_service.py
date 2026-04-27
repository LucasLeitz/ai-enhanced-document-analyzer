import requests

from app.core.config import OLLAMA_BASE_URL, OLLAMA_MODEL

def summarize_text(text: str) -> str:
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": f"Summarize this document clearly:\n\n{text}",
            "stream": False
        }
    )

    data = response.json()

    if "response" not in data:
        raise Exception(f"Ollama error: {data}")

    return data["response"]


def answer_question_about_text(text: str, question: str) -> str:
    prompt = f"""
You are answering a question using only the document text below.

Document:
{text}

Question:
{question}

Answer clearly and concisely. If the answer is not in the document, say that the document does not contain enough information.
"""

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    if "response" not in data:
        raise Exception(f"Ollama error: {data}")

    return data["response"]