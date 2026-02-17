import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import lexiconData from './data/lexicon.json'
import biographiesData from './data/biographies.json'
import candidatesData from './data/candidates.json'

function LexiconView() {
    const [lexicon, setLexicon] = useState([])
    const [biographies, setBiographies] = useState([])
    const [candidates, setCandidates] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    const [activeCategory, setActiveCategory] = useState('All')

    useEffect(() => {
        setLexicon(lexiconData)
        setBiographies(biographiesData)
        setCandidates(candidatesData)
    }, [])

    const categories = ['All', 'Practitioner', 'Text', 'Substance', 'Allegory', 'Apparatus']

    const filteredLexicon = lexicon.filter(item => {
        const matchesSearch = item.term.toLowerCase().includes(searchTerm.toLowerCase()) ||
            item.definition.toLowerCase().includes(searchTerm.toLowerCase())
        const matchesCategory = activeCategory === 'All' || item.definition.includes(`[${activeCategory}]`)
        return matchesSearch && matchesCategory
    })

    // Helper to find entity ID for a term
    const getEntityId = (term) => {
        const candidate = candidates.find(c => c.name.toLowerCase() === term.toLowerCase())
        return candidate ? candidate.id : null
    }

    // Helper to check if biography exists
    const hasBiography = (term) => {
        const entityId = getEntityId(term)
        return biographies.some(b => b.entity_id === entityId)
    }

    return (
        <div className="lexicon-view">
            <header className="glass-panel" style={{ marginBottom: '2rem', display: 'flex', gap: '1rem', alignItems: 'center', flexWrap: 'wrap' }}>
                <input
                    type="text"
                    placeholder="Filter Lexicon..."
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
                <div className="category-filters" style={{ display: 'flex', gap: '0.5rem' }}>
                    {categories.map(cat => (
                        <button
                            key={cat}
                            onClick={() => setActiveCategory(cat)}
                            style={{
                                padding: '0.5rem 1rem',
                                background: activeCategory === cat ? '#D4AF37' : 'rgba(212, 175, 55, 0.1)',
                                color: activeCategory === cat ? '#000' : '#D4AF37',
                                border: '1px solid #D4AF37',
                                borderRadius: '4px',
                                cursor: 'pointer',
                                fontSize: '0.8rem',
                                fontWeight: 'bold'
                            }}
                        >
                            {cat.toUpperCase()}
                        </button>
                    ))}
                </div>
            </header>

            <div className="lexicon-grid" style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
                gap: '1.5rem'
            }}>
                {filteredLexicon.map((item, idx) => {
                    const entityId = getEntityId(item.term)
                    const bioAvailable = hasBiography(item.term)

                    return (
                        <div key={idx} className="glass-panel" style={{
                            padding: '1.5rem',
                            display: 'flex',
                            flexDirection: 'column',
                            justifyContent: 'space-between',
                            borderLeft: item.mention_count > 0 ? '4px solid #D4AF37' : '1px solid rgba(255,255,255,0.1)'
                        }}>
                            <div>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
                                    <h3 style={{ margin: 0, color: '#D4AF37' }}>{item.term}</h3>
                                    {item.mention_count > 0 && (
                                        <span style={{
                                            fontSize: '0.7rem',
                                            background: 'rgba(212, 175, 55, 0.2)',
                                            padding: '0.2rem 0.5rem',
                                            borderRadius: '10px',
                                            color: '#D4AF37'
                                        }}>
                                            {item.mention_count} MENTIONS
                                        </span>
                                    )}
                                </div>
                                <p style={{ fontSize: '0.9rem', lineHeight: '1.5', color: '#F4EBD0', opacity: 0.9 }}>
                                    {item.definition.replace(/\[.*?\] /, '')}
                                </p>
                            </div>
                            <div style={{ marginTop: '1rem', paddingTop: '1rem', borderTop: '1px solid rgba(255,255,255,0.05)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                <span style={{ fontSize: '0.7rem', color: '#888', fontStyle: 'italic' }}>
                                    {item.definition.match(/\[(.*?)\]/)?.[1] || 'GENERAL'}
                                </span>
                                {bioAvailable ? (
                                    <Link to={`/biography/${entityId}`} style={{
                                        background: '#D4AF37',
                                        border: '1px solid #D4AF37',
                                        color: '#000',
                                        fontSize: '0.7rem',
                                        padding: '0.3rem 0.6rem',
                                        borderRadius: '2px',
                                        cursor: 'pointer',
                                        textDecoration: 'none',
                                        fontWeight: 'bold'
                                    }}>
                                        VIEW BIOGRAPHY
                                    </Link>
                                ) : (
                                    <button style={{
                                        background: 'none',
                                        border: '1px solid #444',
                                        color: '#666',
                                        fontSize: '0.7rem',
                                        padding: '0.3rem 0.6rem',
                                        borderRadius: '2px',
                                        cursor: 'not-allowed'
                                    }} disabled>
                                        NO LOG
                                    </button>
                                )}
                            </div>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

export default LexiconView;
