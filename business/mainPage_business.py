#encoding:utf-8
from handle.mainPage_handle import MainHandle
import time

class MainPageBusiness:
    def __init__(self,driver):
        self.mainhandle=MainHandle(driver)
    #取消更新
    def cancel_updata(self):
        time.sleep(10)
        self.mainhandle.cancelUpdate()
    #取消更新，到登录页
    def cancel_to_loginPage(self):
        self.mainhandle.cancelUpdate()
        time.sleep(1)
        self.to_learningPage()
        time.sleep(1)
        self.to_curriculumPage()
        time.sleep(1)
        self.to_myPage()
        time.sleep(1)
        self.to_homePage()
        time.sleep(1)
        self.mainhandle.toLoginPage()
    #去首页
    def to_homePage(self):
        self.mainhandle.toHomePage()
    #去错题集
    def to_learningPage(self):
        self.mainhandle.toLearningPage()
    #去我的课程
    def to_curriculumPage(self):
        self.mainhandle.toCurriculumPage()
    #去我的
    def to_myPage(self):
        self.mainhandle.toMyPage()
    #去登录
    def to_loginPage(self):
        self.mainhandle.toLoginPage()
    #更新应用
    def update_app(self):
        pass

