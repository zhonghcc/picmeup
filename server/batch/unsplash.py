import basespider
from models import Article,User
from utils.constant import *
import re
import json


class Unsplash(basespider.BaseSpider):
    def __init__(self):

        self.collist = None
        self.colIndex = 120
        self.picList = []

    def prepareOneCollection(self):
        colUrl = "https://unsplash.com/collections/curated/"+str(self.colIndex)
        self.colIndex = self.colIndex+1
        picList = self.getPhotosJSON(colUrl)
        return picList


    def getPhotosJSON(self,url):
        colHtml = self.getHtml(url)
        if colHtml == None:
            return None
        j=0
        start=9999
        end=9999
        sb = ""
        for line in colHtml.split('\n'):
            if '__ASYNC_PROPS__' in line:
                start=j
            if j>start and j<end and '</script>' in line:
                end=j
            if j>start and j<end:
                sb=sb+line
            j=j+1
        #sb = sb[0:-2]
        obj0 = json.loads(sb,encoding="utf-8")
        picList = obj0['asyncPropsPhotoFeed']['photos']
        print len(picList)
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

        picUrl = obj['urls']['raw']
        originUrl = obj['links']['html']
        origName = obj['id']
        fileName = origName+'.jpg'

        self.saveImage(picUrl,fileName)

        # self.article = Article()
        # self.article.origin = self.getSource()
        # self.article.origin_url =
        # self.origName = 'minimography_%s_orig.jpg' % self.picName
        # self.article.file_name = self.origName  # minimography_001_orig.jpg
        # self.article.title = self.getSource() + ' ' + self.picName
        return True

    def saveAriticle(self):
        return True

