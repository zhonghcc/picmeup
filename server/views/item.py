# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory
from server import app,db
from models import Article
import os

blueprint = Blueprint('item', __name__)


@blueprint.route('/<id>')
def detail(id):
    article = Article.query.get(id)
    return render_template('item.html',article=article)


