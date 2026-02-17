import sys
import json
from scripts.config_loader import load_config
from scripts.db import init_db
from scripts.ingest_documents import ingest_documents
from scripts.export_data import export_to_json
from scripts.extract_text import extract_and_chunk
from scripts.mine_broad import mine_broad

def print_config():
    """Load and print the effective configuration."""
    try:
        config = load_config()
        print(json.dumps(config.to_dict(), indent=2))
    except Exception as e:
        print(f"Failed to load configuration: {e}")
        sys.exit(1)

def initialize_database():
    """Initialize the database with migrations."""
    try:
        config = load_config()
        init_db(config.db_path)
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize database: {e}")
        sys.exit(1)

def run_ingestion():
    """Run document ingestion."""
    try:
        ingest_documents()
    except Exception as e:
        print(f"Ingestion failed: {e}")
        sys.exit(1)

def run_export():
    """Export document data to JSON."""
    try:
        config = load_config()
        export_to_json(config)
    except Exception as e:
        print(f"Export failed: {e}")
        sys.exit(1)

def run_extraction():
    """Extract text and chunk documents."""
    try:
        config = load_config()
        extract_and_chunk(config)
    except Exception as e:
        print(f"Extraction failed: {e}")
        sys.exit(1)

def run_mining():
    """Perform broad lexicon-based mining."""
    try:
        config = load_config()
        mine_broad(config)
    except Exception as e:
        print(f"Mining failed: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python manage.py [command]")
        print("Commands:")
        print("  print-config    Display the effective configuration values")
        print("  init-db         Initialize the database with migrations")
        print("  ingest          Scan corpus and inventory documents")
        print("  extract         Extract text and chunk documents")
        print("  mine            Perform broad alchemical mining")
        print("  export          Export metadata to JSON for frontend")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == "print-config":
        print_config()
    elif command == "init-db":
        initialize_database()
    elif command == "ingest":
        run_ingestion()
    elif command == "extract":
        run_extraction()
    elif command == "mine":
        run_mining()
    elif command == "export":
        run_export()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
