#-*-coding:utf-8-*-

from Article import Article
from Collection import Collection
from CollectionItem import CollectionItem
from Tag import Tag
from User import User


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")