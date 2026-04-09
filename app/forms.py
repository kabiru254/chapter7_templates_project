from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, SelectField
from wtforms.validators import DataRequired, Length


class StockForm(FlaskForm):
    """Stock Form"""
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_description = StringField('Product Description', validators=[DataRequired()])
    stock_available = SelectField('Stock Available', choices=[('1', '1'), ('5', '5'), ('12','12'), ('20','20')])
    submit = SubmitField('Add Product')

class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Register')