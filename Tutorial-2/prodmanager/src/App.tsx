import React, { useState } from 'react';
import Navigation from './components/Navigation';
import Home from './components/Home';
import Products from './components/Products';
import Contact from './components/Contact';

type PageType = 'home' | 'products' | 'contact';

const App: React.FC = () => {
    const [currentPage, setCurrentPage] = useState<PageType>('home');

    const renderCurrentPage = () => {
        switch (currentPage) {
            case 'home':
                return <Home />;
            case 'products':
                return <Products />;
            case 'contact':
                return <Contact />;
            default:
                return <Home />;
        }
    };

    return (
        <div className="App min-h-screen bg-white">

            <Navigation currentPage={currentPage} setCurrentPage={setCurrentPage} />

            <main>
                {renderCurrentPage()}
            </main>
        </div>
    );
};

export default App;