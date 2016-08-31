import basespider
from models import Article,User
from utils.constant import *
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
        return ORI_MINIMOGRAPHY

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

            # pic_url
            reg = r'http://.*download.*\"'
            imgre = re.compile(reg)
            imglist = re.findall(imgre, html)
            pic_url = imglist[0][0:-1]

            # author_url
            reg = r'http://minimography.com/author/\S+/'
            author_url_re = re.compile(reg)
            author_url = re.findall(author_url_re,html)
            author_url = author_url[0]
            print pic_url
            print author_url

            author = self.getDB().session.query(User).filter(User.origin_url == author_url).first()
            if author is None:
                # author name
                author_html = self.getHtml(author_url)
                reg = '<span itemprop="name">(.+)</span>'
                author_name_re = re.compile(reg)
                author_name = re.findall(author_name_re,author_html)
                author_name = author_name[0]
                print author_name

                #author desc
                reg = '<div class="author-box-content" itemprop="description"><p>(.+)</p>'
                author_desc_re = re.compile(reg)
                author_desc = re.findall(author_desc_re,author_html)
                author_desc = author_desc[0]
                #print author_desc
                dr = re.compile(r'<[^>]+>',re.S)
                author_desc = dr.sub('',author_desc)
                print author_desc

                author = User()
                author.description = author_desc
                author.nickname = author_name
                author.username = author_name
                author.is_imported = True
                author.origin = self.getSource()
                author.origin_url = author_url
                author.status = STATUS_NORMAL
                author.role = ROLE_AUTHOR

                self.saveAuthor(author)
                self.article.author_id = author.id

            self.article.pic_url = pic_url
            return self.saveImage(pic_url, self.origName)
        except Exception, e:
            self.logger.error(e)
            return False

        return True
