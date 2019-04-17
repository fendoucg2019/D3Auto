#coding=utf-8
from airtest.core.api import *
from driver.getDev import getDev
from poco.drivers.unity3d import UnityPoco
import unittest
from BeautifulReport import BeautifulReport
from until.cmpjpg import compare_images
class ZhuanHongbao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.img_path='../snapshot'
        pass
    def setUp(self):
        zhbDev=getDev()
        zhbDev.getDevs()
        set_current(0)
    def save_img(self, img_name):
        self.driver=UnityPoco()
        self.driver.snapshot('{}/{}.png'.format(self.img_path, img_name))
    @BeautifulReport.add_test_img('赚红包与正常UI图不一样的地方截图')
    def test_zhuanhongbao(self):
        '赚红包整个UI显示测试'
        poco=UnityPoco()
        poco("img_redpacket").click()
        snapshot('../snapshot/点击赚红包后截图.jpg')
        clickedzhb ="D:\\work\\3DAuto\\snapshot\\赚红包正常截图 - 副本.jpg"
        zhengchang='D:\\work\\3DAuto\\snapshot\\赚红包正常截图.jpg'
        comparezhb=compare_images(clickedzhb,zhengchang,'../snapshot/赚红包与正常UI图不一样的地方截图.jpg')
        print(comparezhb)
        if comparezhb=='T':
            print('赚红包UI显示正常--测试通过')
        else:
            print('赚红包UI显示不正常--测试不通过')
            assert_equal(clickedzhb,zhengchang,'赚红包UI显示异常')
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass