# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory,jsonify
from server import app,db
from models import Article
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