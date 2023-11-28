from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, index=True)
    description = db.Column(db.Text)
    price = db.Column(db.Float, default=0.0)
    publication_date = db.Column(db.DateTime, default=datetime.now)
    stock_quantity = db.Column(db.Integer, default=1)
    published = db.Column(db.Boolean(), default=True)

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def find_product(cls, product_id):
        product = cls.query.filter_by(id=product_id).first()
        if product:
            return product
        return None
    
    @classmethod
    def find_some_products(cls, products_id):
        products = cls.query.filter(cls.id.in_(products_id)).all()
        if products:
            return products
        return None
