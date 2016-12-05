# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)
from flask import Blueprint, request, session, url_for, redirect, jsonify, abort
from flask import render_template, flash
from flask import current_app as app
from flask_login import current_user,LoginManager
import flask_login as login
from models import User,Article