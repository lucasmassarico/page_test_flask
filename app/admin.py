from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from wtforms.fields import PasswordField
from werkzeug.security import generate_password_hash

from app import db
from app.models.user import User
from app.models.product import Product


class UserView(ModelView):

    # View List Users Settings
    column_searchable_list = ['email']
    column_list = ["id", "name", "email", "password"]
    column_exclude_list = ("password")

    # Edit/Create Views
    edit_modal = True
    create_modal = True

    form_edit_rules = {"name", "email", "password"}

    action_disallowed_list = ['delete']

    def get_edit_form(self):
        form = self.scaffold_form()
        delattr(form, "password")
        form.new_password = PasswordField("Password")
        return form
    
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(form.password.data)
        elif is_created is False:
            if form.new_password.data:
                model.password = generate_password_hash(form.new_password.data)

class DashboardView(AdminIndexView):

    def is_visible(self):
        # This view won't appear in the menu structure
        return False


class ProductView(ModelView):
    # View List Products Settings
    column_searchable_list = ["name"]

    # Edit/Create Views
    edit_modal = True
    create_modal = True


def init_app(admin):
    admin.add_view(UserView(User, db.session))
    admin.add_view(ProductView(Product, db.session))