-- Migration: 0007_time_and_space.sql
-- Description: Adds columns for temporal and spatial data to support Timeline and Map features.

-- 1. Add time_range to entities (e.g., "1520-1541", "17th Century")
ALTER TABLE entities ADD COLUMN time_range TEXT;

-- 2. Add location_data to entities (JSON for coordinates/places, e.g., {"birthplace": "Einsiedeln", "active": ["Basel", "Salzburg"]})
ALTER TABLE entities ADD COLUMN location_data TEXT;

-- 3. Add time_range to biographies (often redundant with lifespan, but useful for 'active period')
ALTER TABLE biographies ADD COLUMN active_period TEXT;

-- 4. Add location_data to biographies (more detailed itinerary)
ALTER TABLE biographies ADD COLUMN locations_json TEXT;

-- 5. Add time_range to documents (for publication year ranges or composition dates)
ALTER TABLE documents ADD COLUMN composition_date TEXT;
