from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddressForm(FlaskForm):
    street = StringField('Street Address: ')
    city = StringField('City: ', validators=[DataRequired()])
    state = StringField('State: ', validators=[DataRequired()])
    zip = StringField('Zip: ')
    submit_Address = SubmitField('Submit')
