# -*- coding: utf-8 -*-


import os
from flask import Flask, render_template, abort, url_for, session
#from flask.ext.openid import OpenID
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_principal import Principal

db = SQLAlchemy()
login_manager = LoginManager()
principals = Principal()
mail = Mail()

app = Flask(__name__)
app.debug_log_format = '[%(levelname)s] %(message)s'
app.debug = True

# Configuration application
def config_app(app, config):
    app.logger.info('Setting up application...')

    app.logger.info('Loading config file: %s' % config)
    app.config.from_pyfile(config)

    app.logger.info('Setting up extensions...')
    db.init_app(app)
    config_principal(app)
    #oid.init_app(app)
    login_manager.init_app(app)
    #babel.init_app(app)
    #mail.init_app(app)
    register_blueprints(app)
    app.run()

    # @babel.localeselector
    # def get_locale():
    #     # 暂时强制返回 zh_CN
    #     return 'zh_CN'

    # from flask.ext.babel import get_locale
    # app.logger.error(get_locale())

    @app.after_request
    def after_request(response):
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500)
        return response

    with app.test_request_context():
        print url_for('index')
        print url_for('user.profile')

def register_blueprints(app):
    app.logger.info('Register blueprints...')
    from views import home,users
    app.register_blueprint(home.blueprint,   url_prefix='')
    app.register_blueprint(users.blueprint,   url_prefix='/users')
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



if __name__ == '__main__':
    config_app(app,'config.cfg')
