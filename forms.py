from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length
from wtforms import StringField, PasswordField

class LoginForm(FlaskForm):
    username = StringField(
        "Username",validators = [InputRequired(), Length(min = 1, max = 20)]
    )
    password = PasswordField(
        "Password", validators = [InputRequired(), Length(min = 6, max = 40)]
    )

class RegisterForm(FlaskForm):
    username = StringField(
        "Username",validators = [InputRequired(), Length(min = 1, max = 20)]
    )
    password = PasswordField(
        "Password", validators = [InputRequired(), Length(min = 6, max = 40)]
    )
    email = StringField(
        "Email", validators = [InputRequired(), Length(max = 50)]
    )
    first_name = StringField(
        "First Name", validators = [InputRequired(), Length(max = 30)]
    )
    last_name = StringField(
        "Last Name", validators = [InputRequired(), Length(max = 30)]
    )

class FeedbackForm(FlaskForm):
    title = StringField(
        "Title", validators = [InputRequired(), Length(max = 100)]
    )
    content = StringField(
        "Content", validators = [InputRequired()]
    )

class DeleteForm(FlaskForm):
    "Delete"