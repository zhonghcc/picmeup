#-*-coding:utf-8-*-

from server import db
from datetime import datetime

class Collection(db.Model):
    __tablename__ = 'collections'

    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    enable = db.Column(db.Boolean,default=True)
