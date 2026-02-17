-- migrations/0002_domain_entities.sql

-- Entities (e.g., Alchemists, Historical Figures)
CREATE TABLE IF NOT EXISTS entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    entity_type TEXT NOT NULL, -- 'alchemist', 'author', 'historical_figure'
    tradition TEXT, -- 'hermetic', 'paracelsian', etc.
    description TEXT,
    is_verified BOOLEAN DEFAULT 0, -- 0 = Candidate, 1 = Verified
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Lexicon (e.g., Symbols, Substances, Terms)
CREATE TABLE IF NOT EXISTS lexicon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term TEXT NOT NULL UNIQUE,
    definition TEXT,
    symbol_path TEXT, -- Path to icon/symbol image
    is_verified BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Mentions (The "Evidence" link between text and entities)
CREATE TABLE IF NOT EXISTS entity_mentions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id INTEGER,
    document_id INTEGER,
    quote TEXT, -- The exact snippet from the text
    page_number INTEGER,
    chunk_index INTEGER,
    confidence_score REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (entity_id) REFERENCES entities(id),
    FOREIGN KEY (document_id) REFERENCES documents(id)
);

-- Linking Lexicon to Mentions (if we want to track terms too)
CREATE TABLE IF NOT EXISTS lexicon_mentions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lexicon_id INTEGER,
    document_id INTEGER,
    quote TEXT,
    page_number INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lexicon_id) REFERENCES lexicon(id),
    FOREIGN KEY (document_id) REFERENCES documents(id)
);
