# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory,request
from server import app,db
from models import *
from auth import current_user
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
    if current_user.is_authenticated:
        view.user_id = current_user.get_id()

    db.session.add(view)
    db.session.commit()
    print author
    return render_template('item.html',article=article,author=author)


