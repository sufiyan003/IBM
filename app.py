from flask import Flask, jsonify

app = Flask(__name__)

# Sample product details
products = {
    "1": {"name": "Laptop", "price": 1000},
    "2": {"name": "Smartphone", "price": 700},
    "3": {"name": "Tablet", "price": 500}
}

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = products.get(id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
