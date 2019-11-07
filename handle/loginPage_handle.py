#encoding:utf-8
from page.login_page import LoginPage

class LoginHandle:
    def __init__(self,driver):
        self.login_page=LoginPage(driver)
    #操作登录页
    #选择手机号登录
    def choosePhoneLogin(self):
        self.login_page.get_phone_login_element().click()
    #输入手机号
    def inputPhone(self,phone):
        self.login_page.get_phone_element().send_keys(phone)
    #点击下一步
    def clickNext(self):
        self.login_page.get_phone_next_element().click()
    #输入密码
    def inputPassword(self,password):
        self.login_page.get_password_element().send_keys(password)
    #点击登录按钮
    def clickLoginBtn(self):
        self.login_page.get_login_btn_element().click()


