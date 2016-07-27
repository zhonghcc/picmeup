# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)
from flask import Blueprint, request, session, url_for, redirect, jsonify, abort
from flask import render_template, flash
from flask import current_app as app
from flask_login import current_user,LoginManager
import flask_login as login

login_manager=LoginManager()
blueprint = Blueprint('user', __name__)


class Anonymous(login.AnonymousUserMixin):
    pass
    #user = User(nickname=u'游客', email='')

class LoginUser(login.UserMixin):
    """Wraps User object for Flask-Login"""

    def __init__(self, user):
        self.id = user.id
        self.user = user

login_manager.anonymous_user = Anonymous
login_manager.login_view = 'user.signin'
login_manager.login_message = u'需要登陆后才能访问本页'


blueprint = Blueprint("user", __name__)

@blueprint.route('/signup/', methods=['GET', 'POST'])
def signup():
    return True


@blueprint.route('/profile/')
@blueprint.route('/profile/<slug_or_id>')
@login.login_required
def profile(slug_or_id=None):
#def profile():
    return True
