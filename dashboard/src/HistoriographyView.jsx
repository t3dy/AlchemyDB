import React, { useState, useEffect } from 'react';

function HistoriographyView() {
    const [scholars, setScholars] = useState([]);
    const [selectedScholar, setSelectedScholar] = useState(null);
    const [filter, setFilter] = useState('all');

    useEffect(() => {
        // Load historian data
        const historiansData = [
            // New Historiography Core
            { name: 'Lawrence M. Principe', affiliation: 'Johns Hopkins University', specialization: 'Experimental reconstruction, Boyle studies', category: 'new-historiography', file: 'principe_bio_prototype.md' },
            { name: 'William R. Newman', affiliation: 'Indiana University', specialization: 'Chymistry, corpuscular theory, George Starkey', category: 'new-historiography', file: 'newman_smith_nummedal_profiles.md' },
            { name: 'Pamela H. Smith', affiliation: 'Columbia University', specialization: 'Artisanal epistemology, Making & Knowing', category: 'new-historiography', file: 'newman_smith_nummedal_profiles.md' },
            { name: 'Tara Nummedal', affiliation: 'Brown University', specialization: 'Economic history, fraud, gender', category: 'new-historiography', file: 'newman_smith_nummedal_profiles.md' },

            // English Alchemy
            { name: 'Jennifer Rampling', affiliation: 'Princeton University', specialization: 'English alchemy, Ripley Scrolls', category: 'english-alchemy', file: 'rampling_kassell_roos_profiles.md' },
            { name: 'Lauren Kassell', affiliation: 'European University Institute', specialization: 'Medical astrology, digital humanities', category: 'english-alchemy', file: 'rampling_kassell_roos_profiles.md' },
            { name: 'Anna Marie Roos', affiliation: 'University of Lincoln', specialization: 'Salt chymistry, Royal Society', category: 'english-alchemy', file: 'rampling_kassell_roos_profiles.md' },

            // Chemical Philosophy
            { name: 'Allen G. Debus', affiliation: 'University of Chicago', specialization: 'Chemical philosophy, Paracelsianism', category: 'chemical-philosophy', file: 'debus_moran_kahn_profiles.md' },
            { name: 'Bruce T. Moran', affiliation: 'University of Nevada, Reno', specialization: 'Court patronage, German alchemy', category: 'chemical-philosophy', file: 'debus_moran_kahn_profiles.md' },
            { name: 'Didier Kahn', affiliation: 'CNRS, Paris', specialization: 'French Paracelsianism, Rosicrucianism', category: 'chemical-philosophy', file: 'debus_moran_kahn_profiles.md' },

            // Literary Scholars
            { name: 'Lyndy Abraham', affiliation: 'Independent Scholar', specialization: 'Alchemical imagery, English literature', category: 'literary', file: 'literary_scholars_profiles.md' },
            { name: 'Stanton J. Linden', affiliation: 'Washington State University', specialization: 'Alchemical poetry, Chaucer', category: 'literary', file: 'literary_scholars_profiles.md' },
            { name: 'Urszula Szulakowska', affiliation: 'University of Leeds', specialization: 'Alchemical imagery, gender studies', category: 'literary', file: 'literary_scholars_profiles.md' },

            // Medieval Specialists
            { name: 'Barbara Obrist', affiliation: 'CNRS Paris, University of Geneva', specialization: 'Medieval manuscripts, iconography', category: 'medieval', file: 'medieval_scholars_profiles.md' },
            { name: 'Michela Pereira', affiliation: 'University of Siena', specialization: 'Medieval alchemy, women in alchemy', category: 'medieval', file: 'medieval_scholars_profiles.md' },
            { name: 'Chiara Crisciani', affiliation: 'University of Pavia', specialization: 'Medieval medical alchemy', category: 'medieval', file: 'medieval_scholars_profiles.md' },

            // Arabic/Islamic
            { name: 'Syed Nomanul Haq', affiliation: 'University of Pennsylvania', specialization: 'Jabir ibn Hayyan, Jabirian philosophy', category: 'arabic', file: 'arabic_scholars_profiles.md' },
            { name: 'Paul Kraus', affiliation: 'Institut Français, Cairo', specialization: 'Jabirian corpus, Arabic philology', category: 'arabic', file: 'arabic_scholars_profiles.md' },
            { name: 'Julius Ruska', affiliation: 'University of Heidelberg', specialization: 'Arabic alchemy, al-Razi', category: 'arabic', file: 'arabic_scholars_profiles.md' },

            // Earlier Historians
            { name: 'Frances Yates', affiliation: 'Warburg Institute', specialization: 'Hermeticism, "Yates Thesis"', category: 'earlier', file: 'earlier_historians_profiles.md' },
            { name: 'Betty Jo Teeter Dobbs', affiliation: 'Northwestern University', specialization: 'Newtonian alchemy', category: 'earlier', file: 'earlier_historians_profiles.md' },
            { name: 'Lynn Thorndike', affiliation: 'Columbia University', specialization: 'Medieval magic, encyclopedism', category: 'earlier', file: 'earlier_historians_profiles.md' },
        ];

        setScholars(historiansData);
    }, []);

    const filteredScholars = filter === 'all'
        ? scholars
        : scholars.filter(s => s.category === filter);

    const categories = [
        { id: 'all', label: 'All Scholars', icon: '📚' },
        { id: 'new-historiography', label: 'New Historiography', icon: '🔬' },
        { id: 'english-alchemy', label: 'English Alchemy', icon: '🏴󠁧󠁢󠁥󠁮󠁧󠁿' },
        { id: 'chemical-philosophy', label: 'Chemical Philosophy', icon: '⚗️' },
        { id: 'literary', label: 'Literary Studies', icon: '📖' },
        { id: 'medieval', label: 'Medieval Specialists', icon: '📜' },
        { id: 'arabic', label: 'Arabic/Islamic', icon: '☪️' },
        { id: 'earlier', label: 'Earlier Historians', icon: '🏛️' },
    ];

    return (
        <div className="historiography-view">
            <div className="view-header">
                <h2>🎓 The New Historiography of Alchemy</h2>
                <p className="view-description">
                    Explore the modern scholars who transformed our understanding of alchemy from "failed chemistry"
                    to a sophisticated natural philosophy integral to the history of science.
                </p>
            </div>

            <div className="filter-bar">
                {categories.map(cat => (
                    <button
                        key={cat.id}
                        className={filter === cat.id ? 'filter-btn active' : 'filter-btn'}
                        onClick={() => setFilter(cat.id)}
                    >
                        {cat.icon} {cat.label}
                    </button>
                ))}
            </div>

            <div className="scholars-grid">
                {filteredScholars.map((scholar, index) => (
                    <div key={index} className="scholar-card">
                        <h3>{scholar.name}</h3>
                        <p className="affiliation">{scholar.affiliation}</p>
                        <p className="specialization">{scholar.specialization}</p>
                        <div className="scholar-meta">
                            <span className="category-badge">{scholar.category}</span>
                        </div>
                    </div>
                ))}
            </div>

            <div className="historiography-footer">
                <p>
                    <strong>Total Scholars: {scholars.length}</strong> |
                    Showing: {filteredScholars.length}
                </p>
                <p className="note">
                    These scholars represent all major authors from the AlchemyDB PDF collection,
                    ensuring comprehensive coverage of the new historiography of alchemy.
                </p>
            </div>

            <style jsx>{`
        .historiography-view {
          max-width: 1200px;
          margin: 0 auto;
          padding: 2rem;
        }

        .view-header {
          text-align: center;
          margin-bottom: 2rem;
        }

        .view-header h2 {
          font-size: 2rem;
          color: #d4af37;
          margin-bottom: 0.5rem;
        }

        .view-description {
          color: #b8b8b8;
          max-width: 800px;
          margin: 0 auto;
          line-height: 1.6;
        }

        .filter-bar {
          display: flex;
          flex-wrap: wrap;
          gap: 0.5rem;
          justify-content: center;
          margin-bottom: 2rem;
          padding: 1rem;
          background: rgba(212, 175, 55, 0.05);
          border-radius: 8px;
        }

        .filter-btn {
          padding: 0.5rem 1rem;
          background: rgba(255, 255, 255, 0.05);
          border: 1px solid rgba(212, 175, 55, 0.3);
          border-radius: 4px;
          color: #e0e0e0;
          cursor: pointer;
          transition: all 0.3s ease;
          font-size: 0.9rem;
        }

        .filter-btn:hover {
          background: rgba(212, 175, 55, 0.1);
          border-color: rgba(212, 175, 55, 0.5);
        }

        .filter-btn.active {
          background: rgba(212, 175, 55, 0.2);
          border-color: #d4af37;
          color: #d4af37;
          font-weight: bold;
        }

        .scholars-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
          gap: 1.5rem;
          margin-bottom: 2rem;
        }

        .scholar-card {
          background: rgba(255, 255, 255, 0.03);
          border: 1px solid rgba(212, 175, 55, 0.2);
          border-radius: 8px;
          padding: 1.5rem;
          transition: all 0.3s ease;
        }

        .scholar-card:hover {
          background: rgba(255, 255, 255, 0.05);
          border-color: rgba(212, 175, 55, 0.4);
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(212, 175, 55, 0.1);
        }

        .scholar-card h3 {
          color: #d4af37;
          margin: 0 0 0.5rem 0;
          font-size: 1.2rem;
        }

        .affiliation {
          color: #b8b8b8;
          font-size: 0.9rem;
          margin: 0.5rem 0;
          font-style: italic;
        }

        .specialization {
          color: #e0e0e0;
          font-size: 0.95rem;
          line-height: 1.5;
          margin: 0.75rem 0;
        }

        .scholar-meta {
          margin-top: 1rem;
          padding-top: 1rem;
          border-top: 1px solid rgba(212, 175, 55, 0.1);
        }

        .category-badge {
          display: inline-block;
          padding: 0.25rem 0.75rem;
          background: rgba(212, 175, 55, 0.1);
          border: 1px solid rgba(212, 175, 55, 0.3);
          border-radius: 12px;
          font-size: 0.75rem;
          color: #d4af37;
          text-transform: uppercase;
          letter-spacing: 0.5px;
        }

        .historiography-footer {
          text-align: center;
          padding: 2rem;
          background: rgba(212, 175, 55, 0.05);
          border-radius: 8px;
          margin-top: 2rem;
        }

        .historiography-footer p {
          margin: 0.5rem 0;
          color: #b8b8b8;
        }

        .historiography-footer strong {
          color: #d4af37;
        }

        .note {
          font-size: 0.9rem;
          font-style: italic;
          max-width: 700px;
          margin: 1rem auto 0;
        }
      `}</style>
        </div>
    );
}

export default HistoriographyView;
