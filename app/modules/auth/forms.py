from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class _AuthForm(FlaskForm):
    email = StringField(label='E-mail', render_kw={'placeholder': 'E-mail'}, validators=[DataRequired(), Length(1, 50)])
    password = PasswordField(label='Password', render_kw={'placeholder': 'Password'}, validators=[DataRequired(), Length(1, 255)])


class LoginForm(_AuthForm):
    submit = SubmitField('Login')


class RegisterForm(_AuthForm):
    name = StringField(label='Name', render_kw={'placeholder': 'Name'}, validators=[DataRequired(), Length(1, 50)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password'), Length(1, 50)])
    submit = SubmitField('Register')
