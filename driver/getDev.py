#coding=utf-8
from airtest.core.android.adb import ADB
from airtest.core.api import *
class getDev():
    def getDevs(self):
        adb=ADB()
        devs=adb.devices()
        if len(devs)>0 and len(devs)<2:
            devs1=devs[0][0]
            print(devs1)
            return devs1
        elif len(devs)==2:
            devs1=devs[0][0]
            devs2=devs[1][0]
            d1=connect_device('Android:///%s'%devs1)
            d2=connect_device('Android:///%s'%devs2)
            print(d1,d2)

            return list(devs1),list(devs2)
        else:
            print(u'没发现手机设备')