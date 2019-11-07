#encoding:utf-8
from configparser import ConfigParser
import os,sys
reload(sys)
class readConfig:
    def __init__(self,path):
        self.path=path
        self.cf = ConfigParser()
        self.cf.read(self.path, encoding="utf-8-sig")


    def getItem(self,item):
        myItem=self.cf.items(item)
        return myItem

    def getValue(self,item,value):
        myValue=self.cf.get(item,value)
        return myValue