# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)
from flask import Blueprint, request, session, url_for, redirect, jsonify, abort
from flask import render_template, flash
from flask import current_app as app

from models import User,Article
from forms.forms import SignupForm,LoginForm
from datetime import datetime
from server import db,login_manager
from utils.constant import *
import auth
import hashlib

blueprint = Blueprint("user", __name__)

@blueprint.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        user = User()

        user.created_time = datetime.now()
        user.email = form.email.data
        user.nickname = form.username.data
        user.username = form.username.data
        user.password = auth.getPassword(user.username,form.password.data)
        user.role = ROLE_DEFAULT
        user.is_imported = False
        user.status = STATUS_NORMAL
        db.session.add(user)
        db.session.commit()
        auth.login(user,True)
        flash(u'注册成功')
        return redirect('/')

    return render_template('usersignup.html',form=form)

@blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class

        user = User.query.filter_by(username=form.username.data,password=auth.getPassword(form.username.data,form.password.data)).first()
        if user != None:

            auth.login(user,form.remember_me.data)
            user.last_log_time = datetime.now()
            db.session.commit()
            flash(u'登录成功')

            next = request.args.get('next')
            # next_is_valid should check if the user has valid
            # permission to access the `next` url
            # if not next_is_valid(next):
            #     return abort(400)
            return redirect(next or url_for('home.index'))

        else:
            flash(u"用户名或密码错误")

    return render_template('userlogin.html', form=form)



@blueprint.route('/profile/')
@blueprint.route('/profile/<id>')
# @login.login_required
def profile(id=None):
#def profile():
    user = User.query.get(id)
    articles = Article.query.filter(Article.author_id==id).offset(0).limit(20).all()
    print articles
    return render_template('userprofile.html',articles=articles,user=user)

@blueprint.route('/logout/')
def logout():
    auth.logout()
    return redirect(url_for('home.index'))