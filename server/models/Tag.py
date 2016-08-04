#-*-coding:utf-8-*-

from server import db
import datetime

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text,nullable=True)

    author_id = db.Column(db.Integer,nullable=True)
    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    published = db.Column(db.Boolean, nullable=False)
