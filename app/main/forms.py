from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length
class PizzaForm(FlaskForm):
    name = SelectField('Pizza name', choices=[('Neapolitan','Neapolitan'),('Chicago','Chicago'),('Greek','Greek'),('New-york','New-york')])
    topping = SelectField('Pizza topping', choices=[('Bacon','Bacon'),('Green Peppers','Green Peppers'),('Mushroom','Mushroom'),('Onions','Onions')])
    crust = SelectField('Pizza crust', choices=[('Chicago style pan','Chicago style pan'),('Pretzel','Pretzel'),('Coast to Coast','Coast to Coast'),('Flat Bread','Flat Bread')])
    submit = SubmitField('Submit')
class StaffForm(FlaskForm):
    name = TextAreaField('update the pizza name.',validators = [Required()])
    topping = TextAreaField('Update the topping section .',validators = [Required()])
    crust = TextAreaField('Update the crust section.',validators = [Required()])
    submit = SubmitField('Submit')
