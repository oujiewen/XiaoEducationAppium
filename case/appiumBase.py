#encoding:utf-8
from appium import webdriver
def getWebdriver(capabilities):
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    return driver

def swiper(driver,list):
    driver.swipe(list[0],list[1],list[2],list[3])

