import { useRef, useState } from "react"
import { Link, useNavigate } from "react-router-dom"

import { uploadDocument } from "../services/documentService"

function UploadPage() {
    const [selectedFile, setSelectedFile] = useState<File | null>(null)
    const [message, setMessage] = useState("")

    const fileInputRef = useRef<HTMLInputElement>(null)
    const navigate = useNavigate()

    function handleUpload() {
        if (!selectedFile) {
            setMessage("Please select a file first.")
            return
        }

        uploadDocument(selectedFile).then(() => {
            setSelectedFile(null)
            setMessage("Document uploaded successfully.")

            if (fileInputRef.current) {
                fileInputRef.current.value = ""
            }

            navigate("/")
        })
    }

    return (
        <section>
            <h2>Upload Document</h2>

            <input
                type="file"
                ref={fileInputRef}
                onChange={(event) => setSelectedFile(event.target.files?.[0] || null)}
            />

            <button onClick={handleUpload}>Upload</button>

            {message && <p>{message}</p>}

            <p>
                <Link to="/">Back to documents</Link>
            </p>
        </section>
    )
}

export default UploadPage