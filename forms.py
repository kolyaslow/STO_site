from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class RequestForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()],
                       render_kw={'class_': 'inp_1'})
    phone_number = StringField('Phone', validators=[InputRequired()],
                               render_kw={'class_': 'inp_2'})
    vin_number = StringField('VIN Number', validators=[InputRequired()],
                             render_kw={'class_': 'inp_3'})

