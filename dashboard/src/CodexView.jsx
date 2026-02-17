import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import CodexLayout from './CodexLayout';
import lexiconData from './data/lexicon.json';

function CodexEntry({ entry }) {
    if (!entry) return <div style={{ color: '#666', fontStyle: 'italic', marginTop: '20vh', textAlign: 'center' }}>Select an entry from the index...</div>;

    return (
        <article className="codex-entry" style={{ animation: 'fadeIn 0.5s ease' }}>
            <header style={{ marginBottom: '2rem', borderBottom: '1px solid #333', paddingBottom: '1rem' }}>
                <div style={{
                    fontSize: '0.8rem',
                    color: '#D4AF37',
                    textTransform: 'uppercase',
                    letterSpacing: '1px',
                    marginBottom: '0.5rem'
                }}>
                    {entry.category || 'Uncategorized'}
                </div>
                <h1 style={{
                    fontFamily: '"Cinzel", serif',
                    fontSize: '3.5rem',
                    margin: 0,
                    color: '#f4ebd0',
                    lineHeight: '1.1'
                }}>
                    {entry.term}
                </h1>
            </header>

            <div className="codex-body" style={{
                fontSize: '1.25rem',
                lineHeight: '1.8',
                color: '#dcdcdc',
                maxWidth: '75ch'
            }}>
                {/* Check if definition is robust (has paragraphs) or simple */}
                {entry.definition.includes('\n') ? (
                    <ReactMarkdown>{entry.definition}</ReactMarkdown>
                ) : (
                    <p>{entry.definition}</p>
                )}
            </div>

            {entry.source === 'abraham' && (
                <div style={{
                    marginTop: '4rem',
                    paddingTop: '1rem',
                    borderTop: '1px solid #333',
                    fontSize: '0.9rem',
                    color: '#666',
                    fontStyle: 'italic'
                }}>
                    Source: Abraham-Style Scholarly Reconstruction
                </div>
            )}
        </article>
    );
}

function CodexView() {
    const [searchTerm, setSearchTerm] = useState('');
    const [selectedId, setSelectedId] = useState(null);
    const [entries, setEntries] = useState([]);

    useEffect(() => {
        // Sort: Scholarly entries first, then alphabetical
        const sorted = [...lexiconData].sort((a, b) => {
            if (a.category === 'Scholarly' && b.category !== 'Scholarly') return -1;
            if (a.category !== 'Scholarly' && b.category === 'Scholarly') return 1;
            return a.term.localeCompare(b.term);
        });
        setEntries(sorted);
        // Select first scholarly entry by default
        const firstScholary = sorted.find(e => e.category === 'Scholarly');
        if (firstScholary) setSelectedId(firstScholary.id);
    }, []);

    const filtered = entries.filter(e =>
        e.term.toLowerCase().includes(searchTerm.toLowerCase())
    );

    const activeEntry = entries.find(e => e.id === selectedId);

    const SidebarContent = (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
            <div style={{ padding: '1rem' }}>
                <input
                    type="text"
                    placeholder="Search Index..."
                    value={searchTerm}
                    onChange={e => setSearchTerm(e.target.value)}
                    style={{
                        width: '100%',
                        padding: '0.8rem',
                        background: '#222',
                        border: '1px solid #444',
                        color: '#fff',
                        fontFamily: '"EB Garamond", serif',
                        fontSize: '1rem'
                    }}
                />
            </div>
            <div className="index-list">
                {filtered.map(entry => (
                    <div
                        key={entry.id}
                        onClick={() => setSelectedId(entry.id)}
                        style={{
                            padding: '0.8rem 1.5rem',
                            cursor: 'pointer',
                            borderLeft: selectedId === entry.id ? '3px solid #D4AF37' : '3px solid transparent',
                            background: selectedId === entry.id ? 'rgba(212, 175, 55, 0.1)' : 'transparent',
                            color: selectedId === entry.id ? '#D4AF37' : '#aaa',
                            transition: 'all 0.2s'
                        }}
                    >
                        <div style={{ fontWeight: selectedId === entry.id ? 'bold' : 'normal' }}>{entry.term}</div>
                        {entry.category === 'Scholarly' && (
                            <span style={{ fontSize: '0.6rem', textTransform: 'uppercase', color: '#666' }}>Scholarly</span>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );

    return <CodexLayout sidebar={SidebarContent} content={<CodexEntry entry={activeEntry} />} />;
}

export default CodexView;
