# forms.py
 
from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired


class AddTaskForm(Form):
	income = IntegerField('Income', validators=[DataRequired()])
	down_payment = IntegerField('Down Payment', validators=[DataRequired()])
	interest_rate = IntegerField('Interest Rate', validators=[DataRequired()])
	