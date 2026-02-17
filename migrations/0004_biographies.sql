-- Migration: 0004_biographies.sql

CREATE TABLE IF NOT EXISTS biographies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id INTEGER NOT NULL UNIQUE,
    full_name TEXT,
    lifespan TEXT,
    tradition TEXT,
    narrative_summary TEXT,
    milestones_json TEXT, -- JSON array of objects
    primary_texts_json TEXT, -- JSON array of strings
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (entity_id) REFERENCES entities(id)
);

-- Index for fast lookup by entity
CREATE INDEX idx_bio_entity ON biographies(entity_id);
