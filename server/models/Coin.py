#-*-coding:utf-8-*-

from server import db
from datetime import datetime

class Coin(db.Model):
    __tablename__ = 'coins'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    direction = db.Column(db.String(50),nullable=False,default="")
    reason = db.Column(db.String(50),nullable=False,default="")
    article_id = db.Column(db.Integer,nullable=True)
    user_id = db.Column(db.Integer,nullable=True)
    ip = db.Column(db.String(50),nullable=True)
    coin_num = db.Column(db.Integer,nullable=True)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Integer, nullable=False,default=1)

