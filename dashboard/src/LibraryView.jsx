import React, { useState, useEffect } from 'react';
import docsData from './exports/docs.json';

function LibraryView() {
    const [searchTerm, setSearchTerm] = useState('');
    const [filteredDocs, setFilteredDocs] = useState(docsData);

    useEffect(() => {
        const lowercasedFilter = searchTerm.toLowerCase();
        const filtered = docsData.filter(item => {
            return (
                item.title.toLowerCase().includes(lowercasedFilter) ||
                (item.author && item.author.toLowerCase().includes(lowercasedFilter)) ||
                (item.description && item.description.toLowerCase().includes(lowercasedFilter))
            );
        });
        setFilteredDocs(filtered);
    }, [searchTerm]);

    return (
        <div className="library-view">
            <header className="view-header">
                <h2>Alchemical Library</h2>
                <div className="guide-box glass-panel">
                    <p><strong>Section Guide:</strong> This view features the <code>documents</code> table of our database. It contains metadata for all 205 PDFs in the corpus, including AI-generated short descriptions extracted from the opening sections of each text. Use the search bar to filter by title, author, or content themes.</p>
                </div>
            </header>

            <div className="search-bar">
                <input
                    type="text"
                    placeholder="Search titles, authors, or descriptions..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="glass-input"
                    style={{ width: '100%', padding: '1rem', marginBottom: '2rem' }}
                />
            </div>

            <div className="library-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '1.5rem' }}>
                {filteredDocs.map(doc => (
                    <div key={doc.id} className="glass-panel scholar-card" style={{ padding: '1.5rem', display: 'flex', flexDirection: 'column' }}>
                        <h3 style={{ color: '#D4AF37', marginTop: 0 }}>{doc.title}</h3>
                        <div style={{ fontSize: '0.8rem', color: '#888', marginBottom: '1rem' }}>
                            <span>{doc.author || 'Unknown Author'}</span> • <span>{doc.year || 'N.D.'}</span> • <span>{doc.doc_type.toUpperCase()}</span>
                        </div>
                        <p style={{ fontSize: '0.9rem', flexGrow: 1, color: '#f4ebd0' }}>{doc.description}</p>
                        <div style={{ marginTop: 'auto', paddingTop: '1rem', fontSize: '0.7rem', color: '#666' }}>
                            DATABASE ID: {doc.id}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default LibraryView;
