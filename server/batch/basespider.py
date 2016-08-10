#-*-coding:utf-8-*-

from server import db,app
from datetime import datetime
from models import Article
import urllib
import re
import os
from PIL import Image
import logging
import sys

class BaseSpider():

    def init(self):
        self.article = Article()

    def getBasePath(self):
        p = os.path.abspath(os.path.dirname(sys.argv[0]))
        return p+"/pics/"

    def getSource(self):
        pass


    def getNext(self):
        pass

    def process(self):
        url = self.getNext()
        while url is not None:
            app.logger.debug(url)
            html = self.getHtml(url)
            result = self.processSingle(url,html)
            if result==None:
                break
            else:
                self.saveAriticle()
                url = self.getNext()

    def saveAriticle(self):
        db.session.add(self.article)
        db.session.commit()

    def processSingle(self,url,html):
        pass

    def getHtml(self,url):
        page = urllib.urlopen(url)
        html = page.read()
        return html

    def saveImage(self,img_url,filename):

        count = db.session.query(Article).filter(Article.pic_url==img_url).count()
        if count>0:
            self.debug(img_url+'already downloaded')
            return True
        path = self.getBasePath()+self.getSource()
        if not os.path.exists(path):   #路径不存在时创建一个
            os.makedirs(path)
        fullPath = path+'/'+filename
        if os.path.exists(fullPath):
            self.debug(fullPath+'already existed')
            return True
        image = urllib.urlretrieve(img_url,fullPath)
        self.genThumbnail(fullPath)


    def genThumbnail(self,filename):
        pass

    def debug(self,msg):
        app.logger.debug(msg)

    def info(self,msg):
        app.logger.info(msg)

    def error(self,msg):
        app.logger.error(msg)
