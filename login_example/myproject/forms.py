from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from myproject.models import User

class RegisterForm(FlaskForm):

    user_name = StringField("User name", validators=[DataRequired()] )
    email = StringField("Email", validators=[DataRequired(), Email() ])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired() , EqualTo('password', message="Please enter matching passwords")])
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email is already registered!")

    def validate_username(self, field):
        if User.query.filter_by(user_name=field.data).first():
            raise ValidationError("Username is taken!")

class LoginForm(FlaskForm):
    
    email = EmailField("Enter your username", validators=[DataRequired()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Login")



