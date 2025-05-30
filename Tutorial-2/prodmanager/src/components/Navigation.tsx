import React from 'react';

interface NavigationProps {
    currentPage: string;
    setCurrentPage: (page: string) => void;
}

const Navigation: React.FC<NavigationProps> = ({ currentPage, setCurrentPage }) => {
    const navItems = [
        { id: 'home', label: 'Home' },
        { id: 'products', label: 'Products' },
        { id: 'contact', label: 'Contact' }
    ];

    return (
        <nav className="bg-white border-b border-gray-200 py-4">
            <div className="max-w-7xl mx-auto px-8">
                <div className="flex justify-between items-center">
                    {/* Logo/Brand */}
                    <button
                        onClick={() => setCurrentPage('home')}
                        className="text-xl font-semibold text-gray-900"
                    >
                        ProdManage
                    </button>

                    <div className="flex space-x-8">
                        {navItems.map((item) => (
                            <button
                                key={item.id}
                                onClick={() => setCurrentPage(item.id)}
                                className={`text-sm font-medium transition-colors ${
                                    currentPage === item.id
                                        ? 'text-blue-600'
                                        : 'text-gray-600 hover:text-gray-900'
                                }`}
                            >
                                {item.label}
                            </button>
                        ))}
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default Navigation;