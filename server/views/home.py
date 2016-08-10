# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response
from server import app,db
from models import Article

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def index():
    articleList = Article.query.all()
    return render_template('index.html',articles=articleList)
