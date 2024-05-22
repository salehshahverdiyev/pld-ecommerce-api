from models import *
from flask import Flask, request, jsonify

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products])


@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify(product.serialize())

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    print(customers)
    return jsonify([customer.serialize() for customer in customers])

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = Customer(name=data['name'], email=data['email'])
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.serialize())

@app.route('/customers/<customer_id>/cart', methods=['POST'])
def add_to_cart(customer_id):
    data = request.get_json()
    cart = Cart(customer_id=customer_id, product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(cart)
    db.session.commit()
    return jsonify(cart.serialize())

@app.route('/customers/<customer_id>/cart', methods=['GET'])
def get_cart(customer_id):
    cart = Cart.query.filter_by(customer_id=customer_id).all()
    return jsonify([c.serialize() for c in cart])

@app.route('/customers/<customer_id>/checkout', methods=['POST'])
def checkout(customer_id):
    cart = Cart.query.filter_by(customer_id=customer_id).all()
    order = Order(customer_id=customer_id)
    db.session.add(order)
    db.session.commit()
    for c in cart:
        order_item = OrderItem(order_id=order.id, product_id=c.product_id, quantity=c.quantity)
        db.session.add(order_item)
    db.session.commit()
    return jsonify(order.serialize())

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.serialize() for order in orders])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
