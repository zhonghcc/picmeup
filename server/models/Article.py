#-*-coding:utf-8-*-

from server import db
from datetime import datetime

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text,nullable=True)
    origin = db.Column(db.String(255),nullable=True)
    file_name = db.Column(db.String(255),nullable=True)
    origin_url = db.Column(db.Text,nullable=True)
    pic_url = db.Column(db.Text,nullable=True)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    published = db.Column(db.Boolean, nullable=False)
    order =  db.Column(db.Integer,nullable=True,default=0)
