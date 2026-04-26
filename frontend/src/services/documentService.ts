import type { Document } from "../types/Document"
import type { SummaryResponse } from "../types/SummaryResponse"
import type { QuestionResponse } from "../types/QuestionResponse"

const API_BASE_URL = "http://localhost:8000"

export function getDocuments(): Promise<Document[]> {
    return fetch(`${API_BASE_URL}/documents`).then((response) => response.json())
}

export function getDocument(id: string): Promise<Document> {
    return fetch(`${API_BASE_URL}/documents/${id}`).then((response) =>
        response.json()
    )
}

export function uploadDocument(file: File): Promise<unknown> {
    const formData = new FormData()
    formData.append("file", file)

    return fetch(`${API_BASE_URL}/documents/upload`, {
        method: "POST",
        body: formData,
    }).then((response) => response.json())
}

export function summarizeDocument(id: string): Promise<SummaryResponse> {
    return fetch(`${API_BASE_URL}/documents/${id}/summarize`, {
        method: "POST",
    }).then((response) => response.json())
}

export function askDocumentQuestion(
    id: string,
    question: string
): Promise<QuestionResponse> {
    return fetch(`${API_BASE_URL}/documents/${id}/ask`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
    }).then((response) => response.json())
}