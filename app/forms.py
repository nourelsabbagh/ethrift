from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms import IntegerField, PasswordField, HiddenField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class Registration(FlaskForm):
    username = TextAreaField('username', validators=[DataRequired(), Length(min=6,max=10)])
    email = TextAreaField('email', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password1')])

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me',validators= [DataRequired()])