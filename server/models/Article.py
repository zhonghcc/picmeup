#-*-coding:utf-8-*-

from server import db
import datetime

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text,nullable=True)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    published = db.Column(db.Boolean, nullable=False)
    order =  db.Column(db.Integer,nullable=True,default=0)
