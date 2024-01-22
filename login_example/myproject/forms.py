from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from models import User

class RegisterForm(FlaskForm):

    user_name = StringField("User name", validators=[DataRequired()] )
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm_password', message="Passwords do not match")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def check_email(self, field):
        if User.query.filter_by(user_name=field.data).first():
            raise ValidationError


class LoginForm(FlaskForm):
    
    email = EmailField("Enter your username", validators=[DataRequired(), Email()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Login")



