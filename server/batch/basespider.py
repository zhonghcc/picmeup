# -*-coding:utf-8-*-

import batch
from batch import db, app
from datetime import datetime
from models import Article,Collection,CollectionItem
import urllib,urllib2
import re
import os
from PIL import Image
import logging
import sys
from utils.constant import THUMBNAIL_LIT_WIDTH, THUMBNAIL_MID_WIDTH


class BaseSpider():
    def init(self):

        self.article = Article()
        app.config.from_pyfile('config.cfg')
        ctx = app.app_context()
        ctx.push()
        db.init_app(app)
        self.logger = self.getLogger()

        # get this collection
        self.collection = db.session.query(Collection).filter(Collection.name == self.getSource()).first()
        if self.collection is None:
            self.collection = Collection()
            self.collection.name=self.getSource()
            self.saveCollection(self.collection)


    def postInit(self):
        pass

    def getBasePath(self):
        p = os.path.abspath(os.path.dirname(sys.argv[0]))
        return p + "/pics/"

    def getSource(self):
        pass

    def getNext(self):
        '''
        next url or object to process
        :return:
            None: nothing
            url: need to get
            object: to save
        '''
        pass

    def process(self):
        self.init()
        self.postInit()
        obj = self.getNext()
        while obj is not None:
            app.logger.debug(obj)
            #html = self.getHtml(url)
            result = self.processSingle(obj)
            if result == False:
                break
            elif result == None:
                obj = self.getNext()
            else:
                self.saveAriticle()
                self.addArticleToCollection(self.collection,result)
                obj = self.getNext()

    def saveAriticle(self):
        db.session.add(self.article)
        db.session.commit()

    def saveAuthor(self,author):
        db.session.add(author)
        db.session.commit()

    def saveCollection(self,col):
        db.session.add(col)
        db.session.commit()

    def addArticleToCollection(self,col,article):
        colItem = CollectionItem()
        colItem.article_id=article.id
        colItem.collection_id = col.id
        db.session.add(colItem)
        db.session.commit()

    def processSingle(self, url, html):
        '''
        process single article
        :param url: where is the pic come from
        :param html: the body of pic html or json object
        :return:
            None: nothing, you can continue.
            False: error, you must stop
            article object: success
        '''
        pass

    def getHtml(self, url):
        logging.debug(url)
        print url
        try:
            page = urllib2.urlopen(url, timeout=50) # wait him longer time
            code = page.code
            if code==200:
                html = page.read()
                return html
            else:
                return None
        except Exception,e:
            logging.info(e)
            return None

    def saveImage(self, img_url, filename):

        count = db.session.query(Article).filter(Article.pic_url == img_url).count()
        if count > 0:
            self.logger.debug(img_url + ' already downloaded')
            return None

        path = self.getBasePath() + self.getSource()
        if not os.path.exists(path):  # 路径不存在时创建一个
            os.makedirs(path)
        fullPath = path + '/' + filename
        logging.debug(fullPath)
        # if os.path.exists(fullPath):
        #     self.debug(fullPath+'already existed')
        #     return None

        image = urllib.urlretrieve(img_url, fullPath)
        self.genThumbnail(path, filename)
        return True

    def genThumbnail(self, path, filename):
        im = Image.open(path + '/' + filename)
        file, ext = os.path.splitext(filename)

        midSize = self.clipimage(im.size, THUMBNAIL_MID_WIDTH)
        im.thumbnail(midSize, Image.ANTIALIAS)
        im.save(path + '/' + file + '_middle' + ext)

        smallSize = self.clipimage(im.size, THUMBNAIL_LIT_WIDTH)
        im.thumbnail(smallSize, Image.ANTIALIAS)
        im.save(path + '/' + file + '_small' + ext)
        return True

    def clipimage(self, size, width):
        ori_width = float(size[0])
        ori_height = float(size[1])
        box = (width, round(ori_height / ori_width * width))

        return box



    def getLogger(self):
        return app.logger

    def getDB(self):
        return db