import { useState, useEffect } from 'react'
import docsData from './data/docs.json'
import candidatesData from './data/candidates.json'

function Discovery() {
    const [documents, setDocuments] = useState([])
    const [candidates, setCandidates] = useState([])
    const [searchTerm, setSearchTerm] = useState('')

    useEffect(() => {
        setDocuments(docsData)
        setCandidates(candidatesData)
    }, [])

    const filteredDocs = documents.filter(doc =>
        doc.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        (doc.file_path && doc.file_path.toLowerCase().includes(searchTerm.toLowerCase()))
    )

    return (
        <div className="discovery-view">
            <header>
                <div className="glass-panel" style={{ marginBottom: '1rem', display: 'flex', gap: '1rem', alignItems: 'center' }}>
                    <input
                        type="text"
                        placeholder="Filter Documents..."
                        className="search-input"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        style={{
                            padding: '0.8rem',
                            background: 'rgba(0,0,0,0.3)',
                            border: '1px solid #D4AF37',
                            color: '#F4EBD0',
                            borderRadius: '4px',
                            flex: 1
                        }}
                    />
                    <div className="stats">
                        <span style={{ color: '#D4AF37' }}>{filteredDocs.length}</span> Documents Ingested
                    </div>
                </div>
            </header>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 350px', gap: '2rem' }}>
                <main>
                    <div className="glass-panel">
                        <h3>The Library Table</h3>
                        <table className="library-table">
                            <thead>
                                <tr>
                                    <th>Title</th>
                                    <th>Type</th>
                                    <th>File Size</th>
                                    <th>Modified</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredDocs.map((doc) => (
                                    <tr key={doc.id}>
                                        <td style={{ fontWeight: 'bold' }}>{doc.title}</td>
                                        <td>{doc.doc_type}</td>
                                        <td>{(doc.file_size / 1024 / 1024).toFixed(2)} MB</td>
                                        <td>{new Date(doc.mtime).toLocaleDateString()}</td>
                                        <td>
                                            <span className="status-badge status-ingested">INGESTED</span>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </main>

                <aside className="specimen-drawer">
                    <div className="glass-panel" style={{ borderLeft: '4px solid #D4AF37', height: 'fit-content' }}>
                        <h3 style={{ margin: 0 }}>The Specimen Drawer</h3>
                        <p style={{ fontSize: '0.8rem', color: '#888', marginBottom: '1.5rem' }}>New entities from Agentic Mining.</p>

                        <div className="specimen-list" style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                            {candidates.length > 0 ? (
                                candidates.map((can, idx) => (
                                    <div key={idx} className="specimen-card" style={{
                                        padding: '1rem',
                                        background: 'rgba(212, 175, 55, 0.05)',
                                        border: '1px solid rgba(212, 175, 55, 0.2)',
                                        borderRadius: '8px'
                                    }}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                                            <span style={{ color: '#D4AF37', fontWeight: 'bold' }}>{can.name}</span>
                                            <span style={{ fontSize: '0.7rem', opacity: 0.6 }}>{can.entity_type}</span>
                                        </div>
                                        <p style={{ fontSize: '0.8rem', margin: '0 0 0.5rem 0', fontStyle: 'italic' }}>{can.tradition}</p>
                                        {can.quote && (
                                            <div style={{
                                                fontSize: '0.75rem',
                                                padding: '0.5rem',
                                                background: 'rgba(0,0,0,0.2)',
                                                borderLeft: '2px solid #D4AF37',
                                                marginTop: '0.5rem',
                                                color: '#bdbdbd'
                                            }}>
                                                "{can.quote}"
                                            </div>
                                        )}
                                    </div>
                                ))
                            ) : (
                                <div style={{ padding: '1rem', textAlign: 'center', border: '1px dashed #444' }}>
                                    No Candidates Found
                                </div>
                            )}
                        </div>
                    </div>
                </aside>
            </div>
        </div>
    )
}

export default Discovery;
