#-*-coding:utf-8-*-

from server import db
import datetime

class User(db.Model):
    __tablename__ = 'users'

    username=db.Column(db.String(255),primary_key=True)
    password=db.Column(db.String(512),nullable=False)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    enable = db.Column(db.Boolean,default=True)
