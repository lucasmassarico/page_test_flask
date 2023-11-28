from flask import render_template

from app.models.product import Product

from . import products


@products.route("/")
def products_list():
    products = Product.query.filter_by(published=True).all()
    return render_template("products/products_list.html", products=products)

@products.route("/<id>")
def show(id):
    product = Product.query.get(id)
    return render_template("/products/product_show.html", product=product)
