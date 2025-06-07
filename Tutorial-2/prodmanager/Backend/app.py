from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# In-memory storage for products
products = [
    {
        'id': str(uuid.uuid4()),
        'title': 'Sample Product 1',
        'image': 'https://via.placeholder.com/300x200',
        'description': 'This is a sample product description',
        'price': 29.99,
        'created_at': datetime.now().isoformat()
    },
    {
        'id': str(uuid.uuid4()),
        'title': 'Sample Product 2',
        'image': 'https://via.placeholder.com/300x200',
        'description': 'Another sample product description',
        'price': 49.99,
        'created_at': datetime.now().isoformat()
    }
]

def validate_product_data(data, is_update=False):
    """Validate product data"""
    errors = []

    if not is_update or 'title' in data:
        if not data.get('title') or not data.get('title').strip():
            errors.append('Title is required')

    if not is_update or 'image' in data:
        if not data.get('image') or not data.get('image').strip():
            errors.append('Image URL is required')
        elif not data.get('image').startswith(('http://', 'https://')):
            errors.append('Image must be a valid URL')

    if not is_update or 'description' in data:
        if not data.get('description') or not data.get('description').strip():
            errors.append('Description is required')

    if not is_update or 'price' in data:
        try:
            price = float(data.get('price', 0))
            if price <= 0:
                errors.append('Price must be a positive number')
        except (ValueError, TypeError):
            errors.append('Price must be a valid number')

    return errors

def find_product_by_id(product_id):
    """Find a product by ID"""
    return next((product for product in products if product['id'] == product_id), None)

# POST /api/products - Add a product
@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Validate data
        errors = validate_product_data(data)
        if errors:
            return jsonify({'error': 'Validation failed', 'details': errors}), 400

        # Create new product
        new_product = {
            'id': str(uuid.uuid4()),
            'title': data['title'].strip(),
            'image': data['image'].strip(),
            'description': data['description'].strip(),
            'price': float(data['price']),
            'created_at': datetime.now().isoformat()
        }

        products.append(new_product)

        return jsonify({
            'message': 'Product created successfully',
            'product': new_product
        }), 201

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# GET /api/products - Get all products
@app.route('/api/products', methods=['GET'])
def get_all_products():
    try:
        return jsonify({
            'message': 'Products retrieved successfully',
            'products': products,
            'count': len(products)
        }), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# GET /api/products/<id> - Get one product
@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = find_product_by_id(product_id)

        if not product:
            return jsonify({'error': 'Product not found'}), 404

        return jsonify({
            'message': 'Product retrieved successfully',
            'product': product
        }), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# PUT /api/products/<id> - Update a product
@app.route('/api/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        product = find_product_by_id(product_id)

        if not product:
            return jsonify({'error': 'Product not found'}), 404

        # Validate data
        errors = validate_product_data(data, is_update=True)
        if errors:
            return jsonify({'error': 'Validation failed', 'details': errors}), 400

        # Update product fields
        if 'title' in data:
            product['title'] = data['title'].strip()
        if 'image' in data:
            product['image'] = data['image'].strip()
        if 'description' in data:
            product['description'] = data['description'].strip()
        if 'price' in data:
            product['price'] = float(data['price'])

        product['updated_at'] = datetime.now().isoformat()

        return jsonify({
            'message': 'Product updated successfully',
            'product': product
        }), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# DELETE /api/products/<id> - Delete a product
@app.route('/api/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        global products

        product = find_product_by_id(product_id)

        if not product:
            return jsonify({'error': 'Product not found'}), 404

        products = [p for p in products if p['id'] != product_id]

        return jsonify({
            'message': 'Product deleted successfully',
            'deleted_product': product
        }), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Product Manager API is running',
        'timestamp': datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    print("Starting Product Manager API...")
    print("Available endpoints:")
    print("- POST /api/products - Create a product")
    print("- GET /api/products - Get all products")
    print("- GET /api/products/<id> - Get one product")
    print("- PUT /api/products/<id> - Update a product")
    print("- DELETE /api/products/<id> - Delete a product")
    print("- GET /api/health - Health check")

    app.run(debug=True, host='localhost', port=5000)