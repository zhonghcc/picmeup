# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, request,flash, redirect, url_for
from server import app,db
from models import *
from flask_login import login_required
from auth import current_user
from utils.constant import STATUS_DELETE,STATUS_NORMAL
from datetime import datetime
import os

blueprint = Blueprint('item', __name__)


@blueprint.route('/<id>')
def detail(id):
    article = Article.query.get(id)
    author = User.query.get(article.author_id)

    article.view_num = article.view_num+1
    view = ArticleView()
    view.article_id=id
    view.ip = request.remote_addr
    isLike = False
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        view.user_id = user_id
        articleLike = ArticleLike.query.filter_by(article_id=id,user_id=user_id,status=STATUS_NORMAL).first()
        if articleLike != None:
            isLike = True

    db.session.add(view)
    db.session.commit()
    return render_template('item.html',article=article,author=author,isLike=isLike)

@blueprint.route('/<id>/like')
@login_required
def like(id):
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        articleLike = ArticleLike.query.filter_by(article_id=id,user_id=user_id,status=STATUS_NORMAL).first()
        if articleLike != None:
            articleLike.status = STATUS_DELETE
            articleLike.updated_time = datetime.now()
            db.session.commit()
            flash(u"您取消赞赏该作品")
            return redirect(url_for('item.detail',id=id))
        else:
            article = Article.query.get(id)
            article.like_num = article.like_num+1
            view = ArticleLike()
            view.article_id=id
            view.user_id = user_id
            db.session.add(view)
            db.session.commit()
            flash(u"您已赞赏该作品")
            return redirect(url_for('item.detail',id=id))