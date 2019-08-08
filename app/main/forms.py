from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length
class PizzaForm(FlaskForm):
    name = SelectField('Pizza name', choices=[('Neapolitan','Neapolitan 1000ksh'),('Chicago','Chicago 1500ksh'),('Greek','Greek 1000ksh'),('New-york','New-york 1700ksh')])
    topping = SelectField('Pizza additional topping', choices=[('Bacon','Bacon 50ksh'),('Green Peppers','Green Peppers 50ksh'),('Mushroom','Mushroom 50ksh'),('Onions','Onions 50ksh'),('no additional toppings','no additional toppings')])
    crust = SelectField('Pizza additional crust', choices=[('Chicago style pan','Chicago style pan 300ksh'),('Pretzel','Pretzel 350ksh'),('Coast to Coast','Coast to Coast 350ksh'),('Flat Bread','Flat Bread 100ksh'),('no additional crust','no additional crust')])
    submit = SubmitField('Submit')
class StaffForm(FlaskForm):
    name = TextAreaField('update the pizza name.',validators = [Required()])
    topping = TextAreaField('Update the topping section .',validators = [Required()])
    crust = TextAreaField('Update the crust section.',validators = [Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write your bio.',validators = [Required()])
    submit = SubmitField('Submit')
