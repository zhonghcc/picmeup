#-*-coding:utf-8-*-

from server import db
from datetime import datetime
from models import Article
import urllib
import re
import os
from PIL import Image

class BaseSpider():

    def init(self):
        self.article = Article()

    def getBasePath(self):
        return "/pics/"

    def getSource(self):
        pass

    def getFirst(self):
        pass

    def getNext(self):
        pass

    def process(self):
        url = self.getFirst()
        while url is not None:
            html = self.getHtml(url)
            result = self.processSingle(url,html)
            if result==None:
                break
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

    def downloadImg(html):
        reg = r'src="(.+?\.jpg)" pic_ext'
        imgre = re.compile(reg)
        imglist = re.findall(imgre, html)
        #定义文件夹的名字
        t = time.localtime(time.time())
        foldername = str(t.__getattribute__("tm_year"))+"-"+str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))
        picpath = 'D:\\ImageDownload\\%s' % (foldername) #下载到的本地目录

        if not os.path.exists(picpath):   #路径不存在时创建一个
            os.makedirs(picpath)
        x = 0
        for imgurl in imglist:
            target = picpath+'\\%s.jpg' % x
            print 'Downloading image to location: ' + target + '\nurl=' + imgurl
            image = urllib.urlretrieve(imgurl, target, schedule)
            x += 1
        return image;

    def saveImage(self,img_url,filename):

        path = self.getBasePath()+self.getSource()
        if not os.path.exists(path):   #路径不存在时创建一个
            os.makedirs(path)
        fullPath = path+'/'+filename
        image = urllib.urlretrieve(img_url,path)
        self.genThumbnail(fullPath)


    def genThumbnail(self,filename):
        pass

