-- Migration: 0007_entity_uniqueness.sql
-- Description: Adds a unique index to entities.name to support ON CONFLICT logic.

CREATE UNIQUE INDEX IF NOT EXISTS idx_entity_name_unique ON entities(name);
