#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:21523",
    # "automationName":"UiAutomator2",
    "app": "F://41.apk",
    # "noReset":"false",
    # "clearSystemFiles":"true"
    # "appWaitActivity":"com.xinghuolive.live/com.xinghuolive.live.SplashActivity"
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
e = ('xpath', "//*[contains(@text,'下次再说')]")
WebDriverWait(driver, 15, 0.1).until(EC.presence_of_element_located(e))
driver.find_element_by_xpath("//*[contains(@text,'下次再说')]").click()
time.sleep(2)
e = ('xpath', "//android.widget.TextView[contains(@index,2)]")
WebDriverWait(driver, 15, 0.1).until(EC.presence_of_element_located(e))
driver.find_element_by_xpath("//android.widget.TextView[contains(@index,2)]").click()