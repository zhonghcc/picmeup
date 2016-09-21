#-*-coding:utf-8-*-

from server import db
from datetime import datetime

class Collection(db.Model):
    __tablename__ = 'collections'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(255),nullable=False)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer,nullable=True)
    #fork_from = db.Column(db.Integer,nullable=True)
    status = db.Column(db.Integer, nullable=False,default=1)
    order =  db.Column(db.Integer,nullable=True,default=0)
