from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flaskblog.database.repositories.user_repository import UserRepository
from flaskblog.messages import register_msgs

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',   validators=[DataRequired(), Length(min=2, max=20)])
    email    = StringField('Email',      validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if current_user.username != username and UserRepository.get_by_username(username.data):
            raise ValidationError(register_msgs.failed_existed_username())

    def validate_email(self, email):
        if current_user.email != email and UserRepository.get_by_email(email.data):
            raise ValidationError(register_msgs.failed_existed_email())