import sqlite3
import json

def export_lexicon_to_json():
    """Export lexicon table to JSON for static site deployment"""
    conn = sqlite3.connect('alchemydb.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT term, category, definition, theoretical_lineage FROM lexicon ORDER BY term')
    rows = cursor.fetchall()
    
    entries = []
    for row in rows:
        entries.append({
            'term': row[0],
            'category': row[1],
            'definition': row[2],
            'body': row[3]
        })
    
    # Write to dashboard public folder
    with open('dashboard/public/lexicon.json', 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    
    print(f"Exported {len(entries)} entries to dashboard/public/lexicon.json")
    conn.close()

if __name__ == '__main__':
    export_lexicon_to_json()
