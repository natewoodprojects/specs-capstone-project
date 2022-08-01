from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, TextAreaField

class RegisterUser(FlaskForm):
    username = StringField("Username: ")
    password = PasswordField("Password: ")
    confirm_password = PasswordField("Retype Password: ")
    email = EmailField("Email: ")
    register = SubmitField("Register User")

class LoginUser(FlaskForm):
    username = StringField("Username: ")
    password = PasswordField("Password: ")
    login = SubmitField("Login")

class CreateItem(FlaskForm):
    item_name = StringField("Name of Item ")
    cost_of_item = StringField("How many $ did it cost? ")
    hours_to_use = StringField("How many hours do you want to put into this? ")
    hours_used = StringField("How many hours have you made?")
    description = TextAreaField("Description (Optional):")
    submit = SubmitField("Create Item")

class EditItem(FlaskForm):
    item_name = StringField("Name of Item ")
    cost_of_item = StringField("How many $ did it cost? ")
    hours_to_use = StringField("How many hours do you want to put into this? ")
    hours_used = StringField("How many hours have you made?")
    edits = SubmitField("Confirm Edits")
    