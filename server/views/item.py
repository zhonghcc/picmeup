# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, request,flash, redirect, url_for
from server import app,db
from models import *
from flask_login import login_required
from auth import current_user
from utils.constant import *
from datetime import datetime
from forms.forms import TagForm
import os

blueprint = Blueprint('item', __name__)


@blueprint.route('/<id>')
def detail(id):
    return itemDetail(id,TagForm())

def itemDetail(id,form=None):
    article = Article.query.get(id)
    author = User.query.get(article.author_id)
    tag = Tag.query.filter_by(article_id=id,status=STATUS_NORMAL).all()
    keywords = ""
    for t in tag:
        keywords =  keywords + t.title + ','

    keywords = keywords[0:-1]
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
    return render_template('item.html',article=article,author=author,isLike=isLike,tags=tag,form=form,keywords=keywords)

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

@blueprint.route('/<id>/addTag',methods=['POST'])
@login_required
def addTag(id):
    form = TagForm()
    if form.validate_on_submit():

        user_id = current_user.get_id()
        title = form.tag.data

        equalOne = Tag.query.filter_by(user_id=user_id,article_id=id,title=title).first()
        if equalOne is not None:
            form.tag.errors.append(u"不能重复添加")
        else:

            tag = Tag()
            tag.article_id=id
            tag.title=form.tag.data
            tag.user_id = user_id
            tag.status = STATUS_NORMAL

            user = User.query.get(user_id)
            user.coin_num = user.coin_num + 1

            coin = Coin()
            coin.coin_num = 1
            coin.article_id = id
            coin.user_id = user_id
            coin.direction = COIN_DIRECTION_DEBIT
            coin.reason = COIN_REASON_ADDTAG
            coin.ip = request.remote_addr

            db.session.add(tag)
            db.session.add(coin)
            db.session.commit()


            flash(u"标签已提交,金币+1")
            app.logger.info(form.tag.data)

    return itemDetail(id,form)