# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, make_response,send_from_directory
from server import app,db
from models import Article
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
        result = send_from_directory('pics/'+source, file+ext)
    return result


