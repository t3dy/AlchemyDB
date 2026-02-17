-- Migration: 0006_socio_economic_schema.sql
-- Description: Expands schema to support socio-economic and political-economic modeling.

-- 1. Expand entities with socio-political dimensions
ALTER TABLE entities ADD COLUMN knowledge_type TEXT; -- textual, artisanal, experimental, political-economic
ALTER TABLE entities ADD COLUMN social_role TEXT; -- court projector, artisan, philosopher, chemist
ALTER TABLE entities ADD COLUMN participation_type TEXT; -- experimental, advisory, speculative

-- 2. Expand biographies for economic context
ALTER TABLE biographies ADD COLUMN knowledge_economy_role TEXT;

-- 3. Lexicon expansion for theoretical lineage
ALTER TABLE lexicon ADD COLUMN theoretical_lineage TEXT;

-- 4. Identity Resolution Table (Aliases)
CREATE TABLE IF NOT EXISTS entity_aliases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id INTEGER NOT NULL,
    alias_name TEXT NOT NULL,
    confidence REAL DEFAULT 1.0,
    FOREIGN KEY (entity_id) REFERENCES entities(id)
);

CREATE INDEX IF NOT EXISTS idx_alias_entity ON entity_aliases(entity_id);
CREATE INDEX IF NOT EXISTS idx_alias_name ON entity_aliases(alias_name);
