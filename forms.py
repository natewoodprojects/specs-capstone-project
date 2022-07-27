from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SubmitObject(FlaskForm):
    name = StringField("Name of Item ")
    cost = StringField("How many $ did it cost? ")
    hours_desired = StringField("How many hours do you want to put into this? ")
    hours_committed = StringField("How many hours have you made?")
