import basespider
from models import Article
import re


class Minimography(basespider.BaseSpider):
    def __init__(self):
        self.currentidx = 0
        indexHtml = self.getHtml('http://minimography.com/search/')
        reg = r'http://minimography.com/\d{3}/'
        imgre = re.compile(reg)
        self.imglist = re.findall(imgre, indexHtml)

    # def postInit(self):
    #     for url in self.imglist: #TODO Here is need to improve
    #         count = self.getDB().session.query(Article).filter(Article.pic_url == url).count()
    #         if count > 0:
    #             self.logger.debug(img_url + 'already downloaded')
    #             self.imglist.remove(url)
    #     print self.imglist

    def getSource(self):
        return "minimography"

    def getNext(self):
        url = self.imglist.pop(0)
        self.picName = url[24:27]
        return url

        # self.currentidx=self.currentidx+1
        # self.picName='%03.d'%self.currentidx
        # return 'http://minimography.com/%s/' % self.picName

    def processSingle(self, url, html):
        try:
            count = self.getDB().session.query(Article).filter(Article.origin_url == url).count()
            if count > 0:
                return None
            self.article = Article()
            self.article.origin = self.getSource()
            self.article.origin_url = url
            self.origName = 'minimography_%s_orig.jpg' % self.picName
            self.article.file_name = self.origName  # minimography_001_orig.jpg
            self.article.title = self.getSource() + ' ' + self.picName
            reg = r'http://.*download.*\"'
            imgre = re.compile(reg)
            imglist = re.findall(imgre, html)
            pic_url = imglist[0][0:-1]

            self.article.pic_url = pic_url
            return self.saveImage(pic_url, self.origName)
        except Exception, e:
            self.logger.error(e)
            return False

        return True
