from app.forms import RegisterForm
from werkzeug.security import generate_password_hash
from flask import redirect, render_template, url_for
from app import db


from app.models.user import User


from . import auth

@auth.route("/users/")
def users():
    users = User.query.all()
    return render_template("users.html", users=users)

    
@auth.route("/users/<int:id>")
def unique_user(id):
    user = User.query.get(id)
    return render_template("user.html", user=user)
        
    
@auth.route ("/users/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User()
        user.name = form.name.data
        user.email = form.email.data
        user.password = generate_password_hash(form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("register.html", form=form)
