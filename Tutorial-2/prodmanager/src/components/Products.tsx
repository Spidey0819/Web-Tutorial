import React from 'react';

interface Product {
    id: number;
    name: string;
    description: string;
    price: number;
    image: string;
}

const Products: React.FC = () => {
    const products: Product[] = [
        {
            id: 1,
            name: "Wireless Headphones",
            description: "Noise cancelling over-ear headphones",
            price: 120,
            image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300&h=200&fit=crop"
        },
        {
            id: 2,
            name: "Smart Watch",
            description: "Smart wearable with health tracking",
            price: 80,
            image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=300&h=200&fit=crop"
        },
        {
            id: 3,
            name: "Laptop",
            description: "14-inch Full HD display, 256GB SSD",
            price: 600,
            image: "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=300&h=200&fit=crop"
        }
    ];

    return (
        <div className="min-h-screen bg-white">
            <div className="max-w-7xl mx-auto p-16">
                <div className="flex justify-end items-center mb-12">
                    <button className="bg-blue-600 text-white px-6 py-2 rounded font-medium hover:bg-blue-700 transition-colors">
                        + Add Product
                    </button>
                </div>

                <div className="grid grid-cols-3 gap-8">
                    {products.map((product) => (
                        <div key={product.id} className="bg-white border rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-shadow">
                            <img
                                src={product.image}
                                alt={product.name}
                                className="w-full h-40 object-cover"
                            />
                            <div className="p-4">
                                <h3 className="font-semibold text-gray-900 mb-2">{product.name}</h3>
                                <p className="text-sm text-gray-600 mb-3">{product.description}</p>
                                <div className="flex items-center justify-between">
                                    <span className="text-lg font-bold text-blue-600">${product.price}</span>
                                    <div className="flex items-center space-x-1">
                                        <div className="w-4 h-3 bg-green-500 rounded-sm"></div>
                                        <div className="w-4 h-3 bg-blue-500 rounded-sm"></div>
                                        <div className="w-4 h-3 bg-red-500 rounded-sm"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Products;