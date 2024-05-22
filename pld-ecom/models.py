from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecom.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    def serialize(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    def serialize(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id
        }
