#-*-coding:utf-8-*-

from server import db
from datetime import datetime

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text,nullable=True)
    article_id = db.Column(db.Integer,nullable=True)
    author_id = db.Column(db.Integer,nullable=True)
    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Integer, nullable=False)
