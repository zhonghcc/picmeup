# -*-coding:utf-8-*-

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Required, Length, Email  , Regexp, EqualTo # 验证器，直接从 wtforms.validators 导入

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class SignupForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    chkpwd = StringField('chkpwd', validators=[DataRequired()])
    email =  StringField('email', validators=[DataRequired(),Email()])

    def validate_chkpwd(self,field):
        if field.chkpwd != field.password:
            raise ValidationError('两次密码输入不一致')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被使用')
