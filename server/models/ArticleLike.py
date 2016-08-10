#-*-coding:utf-8-*-

from server import db
from datetime import datetime

class ArticleLike(db.Model):
    __tablename__ = 'article_likes'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    article_id=db.Column(db.Integer,nullable=False)
    author_id=db.Column(db.Integer,nullable=False)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    enabled = db.Column(db.Boolean, nullable=False,default=True)
