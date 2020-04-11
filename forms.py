from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeField, IntegerField, RadioField, SelectField, HiddenField, TextAreaField, FileField, DateField

from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo

class UserForm(FlaskForm):
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password_chk')])
    password_chk = PasswordField('비밀번호 확인', validators=[DataRequired()])
    name = StringField('이름', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    redirect_url = HiddenField('리다이렉트 URL', validators=[])


class ApiLoginForm(FlaskForm):
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])


class PostForm(FlaskForm):
    title = StringField('제목', validators=[DataRequired()])
    body = TextAreaField('본문', validators=[DataRequired()])