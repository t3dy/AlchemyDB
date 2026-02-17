import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Discovery from './Discovery';
import ProjectLog from './ProjectLog';
import LexiconView from './LexiconView';
import BiographyDetail from './BiographyDetail';
import LibraryView from './LibraryView';
import WhosWhoView from './WhosWhoView';
import HistoriographyView from './HistoriographyView';
import './App.css';

function App() {
  return (
            📚 Library
          </button >
          <button
            className={view === 'historiography' ? 'active' : ''}
            onClick={() => setView('historiography')}
          >
            🎓 Historiography
          </button>
          <button
            className={view === 'discovery' ? 'active' : ''}
            onClick={() => setView('discovery')}
          >
            🔍 Discovery
          </button>
          <button
            className={view === 'log' ? 'active' : ''}
            onClick={() => setView('log')}
          >
            📝 Project Log
          </button>
        </nav >
      </header >
    <main className="App-main">
      {view === 'lexicon' && <LexiconView />}
      {view === 'whos-who' && <WhosWhoView onPersonSelect={handlePersonSelect} />}
      {view === 'biography' && <BiographyDetail person={selectedPerson} onBack={handleBackToWho} />}
      {view === 'library' && <LibraryView />}
      {view === 'historiography' && <HistoriographyView />}
      {view === 'discovery' && <Discovery />}
      {view === 'log' && <ProjectLog />}
    </main>
    </div >
  );
}

export default App;
