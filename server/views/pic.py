# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory,redirect,url_for,flash
from server import app,db
from models import Article
from flask_login import login_required
import os

blueprint = Blueprint('pic', __name__)


@blueprint.route('/<source>/<type>/<fileName>')
def getPic(source,fileName,type):
    app.logger.debug(id)
    file, ext = os.path.splitext(fileName)
    result =None
    if type != 'orig':
        result = send_from_directory('pics/'+source, file+'_'+type+ext)
    else:
        flash(u'您需要登录')
        return redirect(url_for('user.login'))
    return result


@blueprint.route('/download/<source>/<type>/<fileName>')
@login_required
def downloadPic(source,fileName,type):
    app.logger.debug(id)
    file, ext = os.path.splitext(fileName)
    result =None
    if type != 'orig':
        pass
    else:
        result = send_from_directory('pics/'+source, file+ext)
    return result