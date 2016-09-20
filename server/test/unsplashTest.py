#-*-coding:utf-8-*-

import unittest
from batch.unsplash import Unsplash
import app

class UnsplashTest(unittest.TestCase):

    def setUp(self):
        #app.init()
        self.spider = Unsplash()
        self.spider.init()
        self.spider.postInit()
        pass

    def testProcessOne(self):
        url = self.spider.getNext()
        html = self.spider.getHtml(url)
        result = self.spider.processSingle(url,html)
        # print html
        # print result
        self.assertNotEqual(result,False)

    def testProcess(self):
        self.spider.colIndex=120
        self.spider.process()

if __name__ =='__main__':
    unittest.main()