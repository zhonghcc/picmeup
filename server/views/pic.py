# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory,redirect,url_for,flash,request
from server import app,db
from models import *
from flask_login import login_required
from auth import current_user
import os
import time

blueprint = Blueprint('pic', __name__)


@blueprint.route('/<source>/<type>/<fileName>')
def getPic(source,fileName,type):
    file, ext = os.path.splitext(fileName)
    result =None
    # time.sleep(0.5)
    if type != 'orig':
        result = send_from_directory('pics/'+source, file+'_'+type+ext)
    else:
        flash(u'您需要登录')
        return redirect(url_for('user.login'))
    return result


@blueprint.route('/download/<source>/<id>/<fileName>')
@login_required
def downloadPic(source,id,fileName):
    file, ext = os.path.splitext(fileName)
    result =None
    user_id = current_user.get_id()
    downloaded = ArticleDownload.query.filter_by(user_id=user_id,article_id=id).count()
    if downloaded <= 0:
        user = User.query.get(user_id)
        user.coin_num = user.coin_num - 1
        if coin_num < 0 :
            flash(u'下载需要消耗1金币，您的金币不足，给图片添加标签可赚取金币');
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

    article = Article.query.get(id)
    article.download_num = article.download_num+1
    view = ArticleDownload()
    view.article_id=id
    view.ip = request.remote_addr
    if current_user.is_authenticated:
        view.user_id = current_user.get_id()

    db.session.add(view)
    db.session.commit()
    result = send_from_directory('pics/'+source, file+ext)
    return result