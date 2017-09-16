# -*- coding: utf-8 -*-


import os
from flask import Flask, render_template, abort, url_for, session
#from flask.ext.openid import OpenID
from flask_sqlalchemy import SQLAlchemy
import logging
import logging.handlers
from flask_login import LoginManager
from flask_mail import Mail
from flask_principal import Principal

app = Flask(__name__)
log_format = '%(asctime)s [%(levelname)s] [%(filename)s\t%(funcName)s:%(lineno)s] %(message)s'
handler = logging.handlers.TimedRotatingFileHandler('log/picup.log', when='D', interval=1, backupCount=30,  encoding='UTF-8', delay=False, utc=False)
handler.suffix = "%Y%m%d"
handler.setLevel(logging.DEBUG)

logging_format = logging.Formatter(log_format)

handler.setFormatter(logging_format)
app.logger.addHandler(handler)
app.debug = True

db = SQLAlchemy()
principals = Principal()
mail = Mail()



# Configuration application
def config_app(app, config):

    app.logger.info('Setting up application...')

    app.logger.info('Loading config file: %s' % config)
    app.config.from_pyfile(config)
    ctx = app.app_context()
    ctx.push()
    #print app.config['SQLALCHEMY_DATABASE_URI']
    app.logger.info('Setting up extensions...')
    db.init_app(app)

    #print db.get_uri()
    config_principal(app)
    #oid.init_app(app)
    from auth import login_manager
    login_manager.init_app(app)
    #babel.init_app(app)
    #mail.init_app(app)
    register_blueprints(app)




    # @babel.localeselector
    # def get_locale():
    #     # 暂时强制返回 zh_CN
    #     return 'zh_CN'

    # from flask.ext.babel import get_locale
    # app.logger.error(get_locale())
    with app.app_context():
        from datetime import  datetime

        import models
        from models import User
        from models import Article
        #db.create_all()
        print app.config['SQLALCHEMY_DATABASE_URI']
        # User()
        # db.create_all()
        # user=User()
        # user.username='zhonghcc'
        # user.password='123'
        # db.session.add(user)
        print models.User.query.all()
        print app.config['SQLALCHEMY_DATABASE_URI']


        from batch.minimography import Minimography
        from batch import scheduler
        scheduler.start()


        #m=batch.minimography.Minimography()
        #m.process()

    @app.after_request
    def after_request(response):
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500)
        return response

    with app.test_request_context():
        pass
        #print url_for('index')
        #print url_for('user.profile')

def register_blueprints(app):
    app.logger.info('Register blueprints...')
    from views import home,user,item,pic
    app.register_blueprint(home.blueprint,   url_prefix='')
    app.register_blueprint(pic.blueprint,   url_prefix='/pic')
    app.register_blueprint(user.blueprint, url_prefix='/user')
    app.register_blueprint(item.blueprint, url_prefix='/item')
    # app.register_blueprint(events.blueprint, url_prefix='/events')
    # app.register_blueprint(articles.blueprint, url_prefix='/articles')

def config_principal(app):
    principals.init_app(app)

    # 配置 priciple
    from flask_principal import identity_loaded, RoleNeed

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        from flask.ext.login import current_user
        if hasattr(current_user, 'user') and current_user.user.id:
            identity.user = current_user.user
            if hasattr(current_user.user, 'privilege'):
                identity.provides.add(RoleNeed(unicode(current_user.user.privilege)))
                app.logger.info(current_user.user.privilege)
                app.logger.info(identity.provides)


    @principals.identity_loader
    def loadIdentityFromSession():
        if 'identity' in session:
            return session.get('identity')

    @principals.identity_saver
    def save_identity(identity):
        session['identity'] = identity

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


def init():
    config_app(app,'config.cfg')

if __name__ == '__main__':
    init()
    app.run(debug=True, host='0.0.0.0', use_reloader=False)