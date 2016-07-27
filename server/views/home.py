# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response


blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def index():
    return render_template('index.html')
