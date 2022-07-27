from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SubmitObject(FlaskForm):
    name = StringField("Name of Item ")
    cost = StringField("How many $ did it cost? ")
    hours_desired = StringField("How may   ")
    hours_committed = StringField(" ")
