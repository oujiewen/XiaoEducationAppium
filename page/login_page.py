#encoding:utf-8
from util.get_by_local import GetByLocal

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.get_by_local=GetByLocal(driver)
    #获取手机登录方式按钮
    def get_phone_login_element(self):
        return  self.get_by_local.get_element('login_page','phone_login')
    #获取手机号输入框
    def get_phone_element(self):
        return self.get_by_local.get_element('login_page','phone')
    #获取下一步
    def get_phone_next_element(self):
        return self.get_by_local.get_element('login_page','phone_next')
    #获取密码输入框
    def get_password_element(self):
        return self.get_by_local.get_element('login_page','password')
    #获取登录按钮
    def get_login_btn_element(self):
        return self.get_by_local.get_element('login_page','login_btn')



