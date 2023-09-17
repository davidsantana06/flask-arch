from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username: StringField = StringField(
        label='Username',
        validators=[DataRequired(), Length(1, 30)]
    )
    password: PasswordField = PasswordField(
        label='Password',
        validators=[DataRequired(), Length(1, 255)]
    )
    submit = SubmitField('Login')
