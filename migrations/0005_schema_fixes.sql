-- Migration: 0005_schema_fixes.sql
-- Description: Adds missing columns to support advanced features and fixes schema inconsistencies.

-- 1. Add description to documents
ALTER TABLE documents ADD COLUMN description TEXT;

-- 2. Add category to lexicon (properly)
ALTER TABLE lexicon ADD COLUMN category TEXT;

-- 3. Add confidence to entities
ALTER TABLE entities ADD COLUMN confidence REAL DEFAULT 1.0;

-- 4. Ensure entity_type exists on entities (it should, but error suggested issues)
-- SQLite doesn't support IF NOT EXISTS in ALTER TABLE, so we rely on the DB class handling it or just the script.
-- Based on 0002 it exists, but let's be safe and assume it's there.
