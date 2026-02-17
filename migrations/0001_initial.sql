-- migrations/0001_initial.sql

-- Tracking pipeline executions
CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    config_snapshot TEXT, -- JSON snapshot of config used
    status TEXT, -- 'running', 'completed', 'failed'
    message TEXT
);

-- Primary document registry
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER,
    doc_type TEXT DEFAULT 'pdf', -- 'pdf', 'chat', 'human_entry'
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- File-level metadata
CREATE TABLE IF NOT EXISTS document_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER,
    sha256 TEXT UNIQUE,
    file_path TEXT UNIQUE,
    file_size INTEGER,
    mtime DATETIME,
    FOREIGN KEY (document_id) REFERENCES documents(id)
);
