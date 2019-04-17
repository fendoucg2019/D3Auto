#coding=utf-8
from poco.drivers.unity3d import UnityPoco
from airtest.core.api import *
from driver.getDev import getDev
import random
class inputid():
    def inputinfo(self):
        # logget = getDev()
        # logget.getDevs()
        # set_current(0)
        poco = UnityPoco()
        poco("address").offspring("Text").click()
        text('192.168.9.183')
        poco("address").offspring("Text").click()
        poco("port").offspring("Text").click()
        text('36003')
        poco("address").offspring("Text").click()
        poco("change_server_btn").click()
        id = ''.join(str(i) for i in random.sample(range(1, 9), 6))
        poco(text="Enter ID").click()
        text(id)
        poco("change_server_btn").click()
