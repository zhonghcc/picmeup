import basespider
from models import Article,User
from utils.constant import *
import re
import json
import unsplash_id
import time
from sqlalchemy import or_


class Unsplash(basespider.BaseSpider):
    def __init__(self):

        self.collist = None
        self.colIndex = 1
        self.picList = []

    def prepareOneCollection(self):

        colUrl = "https://api.unsplash.com/photos/curated?client_id="+\
                 unsplash_id.APPLICATION_ID+"&page="+str(self.colIndex)

        self.logger.debug(colUrl)
        self.colIndex = self.colIndex+1
        picList = self.getPhotosJSON(colUrl)
        return picList


    def getPhotosJSON(self,url):
        # colHtml = self.getHtml(url)
        # if colHtml == None:
        #     return None
        # j=0
        # start=9999
        # end=9999
        # sb = ""
        # for line in colHtml.split('\n'):
        #     if '__ASYNC_PROPS__' in line:
        #         start=j
        #     if j>start and j<end and '</script>' in line:
        #         end=j
        #     if j>start and j<end:
        #         sb=sb+line
        #     j=j+1
        # #sb = sb[0:-2]
        # obj0 = json.loads(sb,encoding="utf-8")

        try:
            html = self.getHtml(url)
            self.logger.debug(html)
            picList = json.loads(html)#obj0['asyncPropsPhotoFeed']['photos']
            self.logger.debug(picList)
        except Exception,e:
            self.logger.error(e)
            return None


        if len(picList) == 0:
            return None
        else:
            time.sleep(75)#75
            return picList

    def getSource(self):
        return ORI_UNSPLASH

    def getNext(self):
        if len(self.picList)==0:
            tempPicList = self.prepareOneCollection()
            if tempPicList!= None:
                self.picList.extend(tempPicList)
            else:
                return None
        return self.picList.pop(0)

    def processSingle(self, obj):
        try:
            picUrl = obj['urls']['raw']
            originUrl = obj['links']['html']
            origName = obj['id']
            fileName = origName+'.jpg'

            count = self.getDB().session.query(Article).filter(or_(Article.origin_url == originUrl,Article.file_name == fileName)).count()
            if count > 0:
                return None

            user = obj['user']
            author_url =user['links']['html']
            author = self.getDB().session.query(User).filter(User.origin_url == author_url).first()
            if author is None:
                author = User()
                author.description = user['bio']
                author.nickname = user['name']
                author.username = user['username']
                author.is_imported = True
                author.origin = self.getSource()
                author.origin_url = author_url
                author.status = STATUS_NORMAL
                author.role = ROLE_AUTHOR

                self.saveAuthor(author)

            self.article = Article()
            self.article.origin = self.getSource()
            self.article.origin_url = originUrl
            self.article.author_id = author.id
            self.article.pic_url = picUrl
            self.article.file_name = fileName
            self.article.title = origName
            result = self.saveImage(picUrl, fileName)
            if result is True:
                time.sleep(75)#75
                return self.article
            else:
                return result
        except Exception,e:
            self.logger.error(e)
            return False
        return False


