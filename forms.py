from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class RequestForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    phone_number = StringField('Phone', validators=[InputRequired()])
    vin_number = StringField('VIN Number', validators=[InputRequired()])
    service = StringField('Service', validators=[InputRequired()])

