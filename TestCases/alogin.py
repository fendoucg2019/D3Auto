#coding=utf-8
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from until.cmpjpg import compare_images
from driver.getDev import getDev
import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random
citys=''.join(str(i) for i in random.sample(range(1,9),1))
diqus=''.join(str(i) for i in random.sample(range(1,5),1))
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        logget=getDev()
        logget.getDevs()
        set_current(0)
        start_app('com.blackwhalegame.hyj.sichuan')
        time.sleep(20)
        poco=UnityPoco()
        if poco(text="切换服务器").exists():
            from until.TestService import inputid
            callTest=inputid()
            callTest.inputinfo()
        else:
            pass
    # @unittest.skip('跳过')
    def test_alogin(self):
        '选择省份'
        poco=UnityPoco()
        #截图
        # snapshot('../snapshot/选择省份截图.png')
        # time.sleep(5)
        # poco(text="四川省").click()
        # snapshot('../snapshot/选择城市截图.png')
        # d1='D:\\work\\3DAuto\\snapshot\\选择省份截图.png'
        # d2='D:\\work\\3DAuto\\snapshot\\选择城市截图.png'
        # cmp=compare_images(d1,d2,'../snapshot/省与城对比不一样截图.png')
        poco(text="账号登录").click()
        time.sleep(5)
        if poco(text="四川省"):
            poco(text="四川省").click()
            if poco("img_title").get_text() == '选择地区':
                print('选择省份--测试通过')
            else:
                print('选择省份--测试失败')
                assert(poco(text="四川省"))
        else:
            print('没有四川省--测试失败')
            assert(poco(text="四川省"))
    # @unittest.skip('跳过')
    def test_city(self):
        '选择城市测试'
        poco=UnityPoco()
        poco("Content").child("item_1(Clone)")[int(citys)].offspring("text_name_before").click()
        if poco("img_title").get_text() == '选择地区':
            print('选择城市--测试通过')
            poco("btn_initial").click()
        else:
            print('选择地区--测试失败')
            assert (poco("img_title").get_text() == '选择地区')

    # @unittest.skip('跳过')
    def test_city_diqu(self):
        '弹出7天签到界面测试'
        poco=UnityPoco()
        if poco(text="第7天").exists():
            print('每日有礼--测试通过')
        else:
            print('每日有礼--测试失败')
            assert(poco(text="第7天"))
    # @unittest.skip('跳过')
    def test_city_diqu_day(self):
        '点击当天领取金豆'
        poco=UnityPoco()
        if poco("img_green_side").exists():
            poco("img_green_side").click()
            if poco("text").get_text() == '分享再领一次':
                print('签到领豆成功--测试通过')
            else:
                print('签到领豆失败--测试不通过')
                assert(poco("text").get_text() == '分享再领一次')
        else:
            print('签到领取金豆失败--测试不通过')
            assert(poco("img_green_side"))
    # @unittest.skip('跳过')
    def test_city_diqu_day_share(self):
        '分享测试'
        poco = UnityPoco()
        if poco("text").get_text() == '分享再领一次':
            poco("btn_identify").click()
            poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
            if poco("android.widget.LinearLayout").offspring("com.tencent.mm:id/jx").exists():
                print('分享跳转微信正常--测试通过')
                poco("com.tencent.mm:id/kb").click()
                poco("android:id/content").offspring("com.tencent.mm:id/az_").click()
                poco = UnityPoco()
                poco("btn_identify").click()
                poco("img_close").click()
            elif poco("android:id/text1").get_text()=='登录微信':
                print('分享跳转微信正常--测试通过')
                poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
                poco("com.tencent.mm:id/kb").click()
                poco=UnityPoco()
                poco("text").click()
                poco("img_close").click()
            else:
                print('分享跳转微信不正常--测试不通过')
                assert(poco("android:id/text1").get_text()=='登录微信')
        else:
            print('弹出分享失败--测试不通过')
            assert (poco("img_green_side"))


