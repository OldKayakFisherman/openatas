from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Length(1, 100)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me?')
    submit = SubmitField("Log In")

    def __str__(self) -> str:
        result = f'Email: {self.email}'
        result = result + f', Remember Me: {self.remember_me}'

        if self.password:
            result = result + ', Password Supplied'
        else:
            result = result + ', Password Not Supplied'

        return result 