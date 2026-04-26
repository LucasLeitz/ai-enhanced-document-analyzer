import { useEffect, useState } from "react"
import { Link } from "react-router-dom"

import { getDocuments } from "../services/documentService"
import type { Document } from "../types/Document"

function HomePage() {
    const [documents, setDocuments] = useState<Document[]>([])

    useEffect(() => {
        getDocuments().then((data) => setDocuments(data))
    }, [])

    return (
        <section>
            <h2>Saved Documents</h2>

            <Link to="/upload">
                <button>Upload New Document</button>
            </Link>

            {documents.length === 0 ? (
                <p>No documents found.</p>
            ) : (
                <ul>
                    {documents.map((document) => (
                        <li key={document.id}>
                            <Link to={`/documents/${document.id}`}>{document.title}</Link>
                        </li>
                    ))}
                </ul>
            )}
        </section>
    )
}

export default HomePage