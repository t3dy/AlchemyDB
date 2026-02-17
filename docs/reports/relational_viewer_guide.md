# Guide: Inspecting the AlchemyDB Relational Database

Since AlchemyDB uses SQLite, you can use any standard SQL viewer to inspect the `data/archive.db` file. This allows you to explore the relationships between documents, chunks, practitioners, and lexicon entries.

## 1. Recommended Viewers
- **DB Browser for SQLite (Free/Open Source)**: Simple, lightweight, and perfect for quick inspections. [Download here](https://sqlitebrowser.org/).
- **DBeaver (Free Community Edition)**: A more powerful, professional-grade tool for visualizing schemas and running complex queries. [Download here](https://dbeaver.io/).

## 2. How to Connect
1. Open your chosen viewer.
2. Select **Open Database** or **New Connection**.
3. Choose **SQLite** as the database type.
4. Point the tool to: `C:\AlchemyDB\data\archive.db`.

## 3. Key Tables to Explore
- `documents`: Metadata for your PDFs.
- `document_chunks`: The extracted text segments (Coordinate System).
- `entities`: Our practitioners (Agrippa, Masha'allah, etc.).
- `entity_mentions`: The **Evidence Trail** linking practitioners back to specific document chunks.

## 4. Helpful Queries
Try running these in the SQL editor of your viewer:

**Show all practitioners and their supporting quotes:**
```sql
SELECT e.name, em.quote, d.title
FROM entities e
JOIN entity_mentions em ON e.id = em.entity_id
JOIN documents d ON em.document_id = d.id;
```

**Find all text chunks related to a specific document:**
```sql
SELECT chunk_index, page_number, content
FROM document_chunks
WHERE document_id = 1
ORDER BY chunk_index ASC;
```
