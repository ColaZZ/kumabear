# coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField(u'邮件地址', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我(保持登录)')
    submit = SubmitField(u'登录')


class RegistrationForm(FlaskForm):
    email = StringField(u'邮件地址', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField(u'密码', validators=[
        DataRequired(), Length(1, 64), EqualTo('password2', message=u'两次密码必须一致.')])
    password2 = PasswordField(u'确认密码', validators=[DataRequired()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validator_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered.')


# 修改密码
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'旧密码', validators=[DataRequired()])
    password = PasswordField(u'新密码', validators=[
        DataRequired(), Length(1, 64), EqualTo('password2', message=u'两次密码必须一致.')])
    password2 = PasswordField(u'确认密码', validators=[DataRequired()])
    submit = SubmitField(u'注册')


# 重设密码
class PasswordResetRequestForm(FlaskForm):
    email = StringField(u'Email', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField(u'重设密码')


class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'新密码', validators=[
        DataRequired(), Length(1, 64), EqualTo('password2', message=u'两次密码必须一致.')])
    password2 = PasswordField(u'确认密码', validators=[DataRequired()])
    submit = SubmitField(u'重设密码')

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError(u'未知的email地址')


# 更改email
class ChangeEmailForm(FlaskForm):
    email = StringField(u'email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'更改email地址')

    def validate_email(self, field):
        if not User.query.filter_by(password=field.data).first():
            raise ValidationError(u'email已经注册过了')

