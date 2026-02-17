-- migrations/0003_document_chunks.sql

-- Stores segments of text extracted from documents
CREATE TABLE IF NOT EXISTS document_chunks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER,
    chunk_index INTEGER,
    content TEXT NOT NULL,
    page_number INTEGER,
    token_count INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id) REFERENCES documents(id)
);

-- Index for faster retrieval by document
CREATE INDEX IF NOT EXISTS idx_chunks_doc ON document_chunks(document_id);
