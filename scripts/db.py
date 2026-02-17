import sqlite3
import os
from pathlib import Path
from typing import List

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path
        # Ensure directory exists
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def run_migration(self, sql_file: str):
        migration_name = Path(sql_file).name
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Ensure migration table exists
            cursor.execute("CREATE TABLE IF NOT EXISTS schema_migrations (name TEXT PRIMARY KEY)")
            
            # Check if already applied
            cursor.execute("SELECT 1 FROM schema_migrations WHERE name = ?", (migration_name,))
            if cursor.fetchone():
                return False # Already applied
                
            with open(sql_file, 'r') as f:
                scripts = f.read()
                conn.executescript(scripts)
            
            cursor.execute("INSERT INTO schema_migrations (name) VALUES (?)", (migration_name,))
            conn.commit()
            return True

def init_db(db_path: str, migration_dir: str = "migrations"):
    db = Database(db_path)
    migrations = sorted(Path(migration_dir).glob("*.sql"))
    for migration in migrations:
        if db.run_migration(str(migration)):
            print(f"Applied migration: {migration.name}")
        else:
            print(f"Migration already applied: {migration.name}")
if __name__ == "__main__":
    import sys
    from scripts.config_loader import load_config
    
    if len(sys.argv) > 1 and sys.argv[1] == "init-db":
        config = load_config()
        init_db(config.db_path)
    else:
        print("Usage: python -m scripts.db init-db")
