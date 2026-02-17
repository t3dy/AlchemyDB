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
        with self.get_connection() as conn:
            with open(sql_file, 'r') as f:
                conn.executescript(f.read())
            conn.commit()

def init_db(db_path: str, migration_dir: str = "migrations"):
    db = Database(db_path)
    migrations = sorted(Path(migration_dir).glob("*.sql"))
    for migration in migrations:
        print(f"Applying migration: {migration.name}")
        db.run_migration(str(migration))
