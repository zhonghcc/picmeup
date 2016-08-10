#-*-coding:utf-8-*-

import batch
from batch import db,app
from datetime import datetime
from models import Article
import urllib
import re
import os
from PIL import Image
import logging
import sys
from utils.constant import THUMBNAIL_LIT_WIDTH,THUMBNAIL_MID_WIDTH

class BaseSpider():

    def init(self):
        self.article = Article()
        app.config.from_pyfile('config.cfg')
        ctx = app.app_context()
        ctx.push()
        db.init_app(app)

    def getBasePath(self):
        p = os.path.abspath(os.path.dirname(sys.argv[0]))
        return p+"/pics/"

    def getSource(self):
        pass


    def getNext(self):
        pass

    def process(self):
        self.init()
        url = self.getNext()
        while url is not None:
            app.logger.debug(url)
            html = self.getHtml(url)
            result = self.processSingle(url,html)
            if result==False:
                break
            elif result==None:
                url = self.getNext()
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
            return None

        path = self.getBasePath()+self.getSource()
        if not os.path.exists(path):   #路径不存在时创建一个
            os.makedirs(path)
        fullPath = path+'/'+filename
        if os.path.exists(fullPath):
            self.debug(fullPath+'already existed')
            return None

        image = urllib.urlretrieve(img_url,fullPath)
        self.genThumbnail(path,filename)


    def genThumbnail(self,path,filename):
        im = Image.open(path+'/'+filename)
        file, ext = os.path.splitext(filename)

        midSize = self.clipimage(im.size,THUMBNAIL_MID_WIDTH)
        im.thumbnail(midSize, Image.ANTIALIAS)
        im.save(path+'/'+file+'_middle' + ext)

        smallSize = self.clipimage(im.size,THUMBNAIL_LIT_WIDTH)
        im.thumbnail(smallSize, Image.ANTIALIAS)
        im.save(path+'/'+file+'_small' + ext)
        return True

    def clipimage(self,size,width):
        ori_width = float(size[0])
        ori_height = float(size[1])
        box = (width,round(ori_height/ori_width*width))

        return box

    def debug(self,msg):
        app.logger.debug(msg)

    def info(self,msg):
        app.logger.info(msg)

    def error(self,msg):
        app.logger.error(msg)
