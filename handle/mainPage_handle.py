#encoding:utf-8
from page.main_page import MainPage

class MainHandle:
    def __init__(self,driver):
        self.main_page=MainPage(driver)
    #操作主页
    #取消更新
    def cancelUpdate(self):
        self.main_page.get_cancel_update_element().click()
    #去登录页
    def toLoginPage(self):
        self.main_page.get_login_btn_element().click()
    #去首页
    def toHomePage(self):
        self.main_page.get_homepage_element().click()
    #去错题集页
    def toLearningPage(self):
        self.main_page.get_learning_element().click()
    #去我的课程页
    def toCurriculumPage(self):
        self.main_page.get_curriculum_element().click()
    #去我的页面
    def toMyPage(self):
        self.main_page.get_my_element().click()

