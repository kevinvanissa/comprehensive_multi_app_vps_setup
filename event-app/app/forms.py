from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, validators, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])


class SignupForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password', message='Passwords must match')])

