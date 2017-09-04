# -*- coding: utf-8 -*-
from flask_login import current_user,LoginManager,login_user,logout_user
import flask_login as login
from flask_login import login_manager
from models import User

login_manager = LoginManager()

class Anonymous(login.AnonymousUserMixin):
    pass
    #user = User(nickname=u'游客', email='')

class LoginUser(login.UserMixin):
    """Wraps User object for Flask-Login"""

    def __init__(self, user):
        self.id = user.id
        self.user = user

login_manager.anonymous_user = Anonymous
login_manager.login_view = 'user.login'
login_manager.login_message = u'需要登录后才能访问本页'

@login_manager.user_loader
def load_user(userid):
    user = User.query.get(userid)
    print(user)
    loginUser = LoginUser(user)
    return loginUser


def login(user,remember_me):
    logedUser = LoginUser(user)
    login_user(logedUser,remember_me)

def logout():
    logout_user()
