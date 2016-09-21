#-*-coding:utf-8-*-

from server import db
from datetime import datetime

class CollectionItem(db.Model):
    __tablename__ = 'collection_items'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    collection_id = db.Column(db.Integer,nullable=False)
    article_id = db.Column(db.Integer,nullable=False)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Integer, nullable=False,default=1)
    order =  db.Column(db.Integer,nullable=True,default=0)
