#-*-coding:utf-8-*-

from server import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nickname=db.Column(db.String(255),nullable=False,unique=True)
    username=db.Column(db.String(255),nullable=False,unique=True)
    password=db.Column(db.String(512),nullable=False)
    last_log_time=db.Column(db.DateTime,nullable=True),

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    published = db.Column(db.Boolean, nullable=False)
