import { Link, Route, Routes } from "react-router-dom"

import DocumentPage from "./pages/DocumentPage"
import HomePage from "./pages/HomePage"
import UploadPage from "./pages/UploadPage"

function App() {
    return (
        <main>
            <header>
                <Link to="/">
                    <h1>AI Enhanced Document Analyzer</h1>
                </Link>

                <p>
                    Upload documents, view saved documents, summarize content, and ask
                    questions about uploaded files.
                </p>
            </header>

            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/upload" element={<UploadPage />} />
                <Route path="/documents/:id" element={<DocumentPage />} />
            </Routes>
        </main>
    )
}

export default App