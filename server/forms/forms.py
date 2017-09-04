# -*-coding:utf-8-*-

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,PasswordField,ValidationError
from wtforms.validators import DataRequired, Required, Length, Email  , Regexp, EqualTo  # 验证器，直接从 wtforms.validators 导入
from models.User import User

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(message=u"请输入用户名")])
    password = PasswordField('password', validators=[DataRequired(message=u"请输入密码")])

    remember_me = BooleanField('remember_me', default=False)

class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(message=u"请输入用户名")])
    password = PasswordField('password', validators=[DataRequired(message=u"请输入密码"), Length(6, 12, message=u'密码长度在6到12位')])
    chkpwd = PasswordField('chkpwd', validators=[DataRequired(message=u"请输入确认密码"),Length(6, 12, message=u'密码长度在6到12位'),EqualTo('password', message=u'密码必须一致')])
    email =  StringField('email', validators=[DataRequired(message=u"请输入邮箱"),Email()])
    notify = BooleanField('notify', default=True)


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已被使用')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已被注册')