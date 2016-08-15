# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory
from server import app,db
from models import Article
import os

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def index():
    articleList = Article.query.offset(0).limit(20).all()
    return render_template('index.html',articles=articleList)

