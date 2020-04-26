from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.database.repositories.UserRepository import UserRepository
from flaskblog.messages import register_msgs

class RegisterationForm(FlaskForm):
    username = StringField('Username',   validators=[DataRequired(), Length(min=2, max=20)])
    email    = StringField('Email',      validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if UserRepository.get_by_username(username.data):
            raise ValidationError(register_msgs.failed_existed_username())

    def validate_email(self, email):
        if UserRepository.get_by_email(email.data):
            raise ValidationError(register_msgs.failed_existed_email())