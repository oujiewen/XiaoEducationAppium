#encodin:utf-8
import time
from appium import webdriver
from util.yamlConfig import YamlClss

class BaseDriver:
    def get_android_driver(self,i):
        yamls = YamlClss()
        # print yamls.get_value('server_1', 'device')
        deviceName=yamls.get_value('server_'+str(i), 'device')
        port = yamls.get_value('server_'+str(i), 'port')
        # print port,type(port)
        capabilities = {
            "platformName": "Android",
            "deviceName": deviceName,
            "automationName":"UiAutomator2",
            "app": "F://41.apk",
            # "noReset":"false",
            # "clearSystemFiles":"true"
            # "appWaitActivity":"com.xinghuolive.live/com.xinghuolive.live.SplashActivity"
          }
        driver = webdriver.Remote("http://127.0.0.1:"+str(port)+"/wd/hub", capabilities)
        return driver