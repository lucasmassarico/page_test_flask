from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        DataRequired("O campo é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(min=8, message="O campo deve conter mais que 8 caracters.")
    ])
    submit = SubmitField("Cadastrar")