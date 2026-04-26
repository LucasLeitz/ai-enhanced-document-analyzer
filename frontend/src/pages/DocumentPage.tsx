import { useEffect, useState } from "react"
import { Link, useParams } from "react-router-dom"

import {
    askDocumentQuestion,
    getDocument,
    summarizeDocument,
} from "../services/documentService"
import type { Document } from "../types/Document"

function DocumentPage() {
    const { id } = useParams()

    const [document, setDocument] = useState<Document | null>(null)
    const [summary, setSummary] = useState("")
    const [question, setQuestion] = useState("")
    const [answer, setAnswer] = useState("")
    const [loadingSummary, setLoadingSummary] = useState(false)
    const [loadingAnswer, setLoadingAnswer] = useState(false)

    useEffect(() => {
        if (!id) return

        getDocument(id).then((data) => setDocument(data))
    }, [id])

    function handleSummarize() {
        if (!id) return

        setLoadingSummary(true)

        summarizeDocument(id).then((data) => {
            setSummary(data.summary)
            setLoadingSummary(false)
        })
    }

    function handleAskQuestion() {
        if (!id || !question.trim()) return

        setLoadingAnswer(true)

        askDocumentQuestion(id, question).then((data) => {
            setAnswer(data.answer)
            setLoadingAnswer(false)
        })
    }

    if (!document) {
        return (
            <section>
                <p>Loading document...</p>
            </section>
        )
    }

    return (
        <section>
            <h2>{document.title}</h2>

            <p>
                <Link to="/">Back to documents</Link>
            </p>

            <h3>AI Tools</h3>

            <button onClick={handleSummarize} disabled={loadingSummary}>
                {loadingSummary ? "Summarizing..." : "Summarize This Document"}
            </button>

            {summary && (
                <div>
                    <h4>Summary</h4>
                    <p>{summary}</p>
                </div>
            )}

            <div>
                <h4>Ask a Question</h4>

                <input
                    type="text"
                    value={question}
                    placeholder="Ask something about this document..."
                    onChange={(event) => setQuestion(event.target.value)}
                />

                <button onClick={handleAskQuestion} disabled={loadingAnswer}>
                    {loadingAnswer ? "Asking..." : "Ask"}
                </button>

                {answer && (
                    <div>
                        <h4>Answer</h4>
                        <p>{answer}</p>
                    </div>
                )}
            </div>

            <h3>Content</h3>

            <pre>{document.content}</pre>
        </section>
    )
}

export default DocumentPage