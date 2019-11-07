#encoding:utf-8
from util import readConfig

class GetByLocal:
    def __init__(self,driver):
        self.driver=driver
    def get_element(self,section,key):
        myCf = readConfig.readConfig('../config/LocalElement.ini')
        local= myCf.getValue(section, key)
        print local
        by=local.split('>')[0]
        local_by=local.split('>')[1]
        print by,local_by,'element info'
        if by=='id':
            element=self.driver.find_element_by_id(local_by)
            return element
        elif by=='class':
            element = self.driver.find_element_by_class(local_by )
        elif by=='xpath':
            element = self.driver.find_element_by_xpath(local_by)
            return element
        elif by=='uiautomator':
            element = self.driver.find_element_by_android_uiautomator(local_by)
            return element

