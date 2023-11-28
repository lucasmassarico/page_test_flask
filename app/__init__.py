import os

from flask import Flask, redirect
from flask_admin import Admin
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from app.config import Config


db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__)
    # load settings
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect('/login')

    # routes
    from app import routes
    routes.init_app(app)

    # register admin page
    import app.admin as administrator

    from app.admin import DashboardView
    admin = Admin(app, name="Antiquário", template_mode="bootstrap4", index_view=DashboardView())
    administrator.init_app(admin)

    return app
