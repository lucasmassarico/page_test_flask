from app.auth import auth as auth_blueprint
from app.product import products as products_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(products_blueprint)

    