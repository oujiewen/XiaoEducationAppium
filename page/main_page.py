#encoding:utf-8
from util.get_by_local import GetByLocal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self,driver):
        self.get_by_local=GetByLocal(driver)
        self.driver=driver
    #获取主页的所有元素
    def get_cancel_update_element(self):
        e = ('xpath', "//*[contains(@text,'下次再说')]")
        WebDriverWait(self.driver, 15, 0.1).until(EC.presence_of_element_located(e))
        return  self.get_by_local.get_element('main_activity','nexttime')
    #获取首页tab
    def get_homepage_element(self):
        return self.get_by_local.get_element('main_activity','homepage')
    #获取错题本tab
    def get_learning_element(self):
        return self.get_by_local.get_element('main_activity','learning')
    #获取我的课程tab
    def get_curriculum_element(self):
        return self.get_by_local.get_element('main_activity','curriculum')
    #获取我的tab
    def get_my_element(self):
        return self.get_by_local.get_element('main_activity','my')
    # 获取登录按钮
    def get_login_btn_element(self):
        return self.get_by_local.get_element('main_activity', 'to_login_btn')


