# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory
from server import app,db
from models import Article
import os

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def index():
    articleList = Article.query.all()
    return render_template('index.html',articles=articleList)

@blueprint.route('/pic/<source>/<fileName>')
def showPic(source,fileName):
    app.logger.debug(id)
    file, ext = os.path.splitext(fileName)
    return send_from_directory('pics/'+source, file+'_small'+ext)
