from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User
from passlib.hash import pbkdf2_sha256


def invalid_credentials(form, field):
    username_entered = form.username.data
    password_entered = field.data

    # Check Username is valid
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError('Usename or Password is incorrect')
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError('Usename or Password is incorrect')



class RegistrationForm(FlaskForm):
    '''Registration Form'''

    username = StringField('username_label',
    validators=[
        InputRequired(message="Username Required"),
        Length(min=4, max=25, message="Username must be between 4 and 25 characters"),
    ])


    password = PasswordField('password_label',
    validators=[
        InputRequired(message="Password Required"),
        Length(min=4, max=25, message="Password must be between 4 and 25 characters"),
    ])


    confirm_pswd = PasswordField('confirm_pswd_label',
    validators=[
        InputRequired(message="Password Required"),
        Length(min=4, max=25, message="Password must match"),
    ])

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise "Username already exists. Select a different username."

    submit_button = SubmitField('Create')




class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField('username', validators=[InputRequired(message="Username required")])
    password = PasswordField('password', validators=[InputRequired(message="Password required"), invalid_credentials])
    submit_button = SubmitField('Login')


