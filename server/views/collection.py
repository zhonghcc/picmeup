# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory
from server import app,db
from models import Article,User
import os

blueprint = Blueprint('collection', __name__)


@blueprint.route('/<id>')
def list(id):
    articles = Article.query.filter(Article.author_id==id).offset(0).limit(20).all()
    print articles
    return render_template('userprofile.html',articles=articles,user=user)



