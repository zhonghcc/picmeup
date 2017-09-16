# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory,jsonify,request
from server import app,db
from models import Article,Tag
from flask_login import login_required
from forms.forms import SearchForm
import logging
import os

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def index():
    articleList = Article.query.order_by(Article.id.desc()).offset(0).limit(20).all()
    totalcount = Article.query.count()
    return render_template('index.html',articles=articleList,totalcount =totalcount,readedpage=1)

@blueprint.route('/page/<int:pageid>')
def page(pageid):
    app.logger.debug(pageid)
    start = int(int(pageid-1)*20)
    app.logger.debug(start)
    articleList = Article.query.order_by(Article.id.desc()).offset(start).limit(20).all()
    app.logger.debug(articleList)
    totalcount = Article.query.count()
    return render_template('index.html',articles=articleList,totalcount=totalcount,readedpage=pageid)
    #return jsonify([i.serialize for i in articleList])

@blueprint.route('/about')
def about():
    return render_template('about.html')

@blueprint.route('/search',methods=['POST'])
@login_required
def search():
    key = request.form['key']
    app.logger.info("search key="+key + str(len(key)))
    if len(key) > 0:
        articleList = []
        tags = db.session.query(Tag).filter(Tag.title.like('%'+key+'%')).offset(0).limit(20).all()
        if len(tags)>0:
            for tag in tags:
                article = Article.query.get(tag.article_id)
                articleList.append(article)
            return render_template('search.html',articles=articleList,isDefault = False,key=key)

    articleList = Article.query.order_by(Article.id.desc()).offset(0).limit(20).all()
    totalcount = Article.query.count()
    return render_template('search.html',articles=articleList,isDefault = True)

@blueprint.route('/explore')
def explore():
    articleList = Article.query.order_by(Article.view_num.desc()).offset(0).limit(20).all()
    totalcount = Article.query.count()
    return render_template('explore.html',articles=articleList,totalcount =totalcount,readedpage=1)