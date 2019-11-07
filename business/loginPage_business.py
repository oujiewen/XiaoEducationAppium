#encoding:utf-8
from handle.loginPage_handle import LoginHandle
import time

class LoginPageBusiness:
    def __init__(self,driver):
        self.loginhandle=LoginHandle(driver)
    #正常登录
    def phone_login_success(self,phone,password):
        self.loginhandle.choosePhoneLogin()
        time.sleep(1)
        self.loginhandle.inputPhone(phone)
        time.sleep(1)
        self.loginhandle.clickNext()
        time.sleep(1)
        self.loginhandle.inputPassword(password)
        time.sleep(1)
        self.loginhandle.clickLoginBtn()
    #错误用户名登录
    def to_homePage(self):
        pass


