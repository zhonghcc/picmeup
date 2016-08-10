
import basespider
from models import Article
import re

class Minimography(basespider.BaseSpider):

    def __init__(self):
        self.currentidx = 0

    def getSource(self):
        return "minimography"

    def getNext(self):
        self.currentidx=self.currentidx+1
        self.picName='%03.d'%self.currentidx
        return 'http://minimography.com/%s/' % self.picName

    def processSingle(self,url,html):
        try:
            self.article = Article()
            self.article.origin=self.getSource()
            self.article.origin_url=url
            self.origName='minimography_%03.d_orig.jpg'%self.currentidx
            self.article.file_name=self.origName #minimography_001_orig.jpg
            self.article.title=self.getSource()+' '+self.picName
            reg=r'http://.*download.*\"'
            imgre = re.compile(reg)
            imglist = re.findall(imgre, html)
            pic_url = imglist[0][0:-1]

            self.article.pic_url=pic_url
            self.saveImage(pic_url,self.origName)
        except Exception,e:
            self.error(e)
            return None

        return True


