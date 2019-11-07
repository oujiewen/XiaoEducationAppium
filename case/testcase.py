#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
from base.base_driver import BaseDriver
from business.mainPage_business import MainPageBusiness
from business.loginPage_business import LoginPageBusiness
import unittest
import HTMLTestRunner
import multiprocessing
from util.server import Server
from util.get_by_local import GetByLocal





# main_business.cancel_to_loginPage()
# login_business.phone_login_success('18042460809','a5565473')
class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName='runTest',parame=None):
		super(ParameTestCase,self).__init__(methodName)
		global parames
		parames = parame

class CaseTest(ParameTestCase):
  @classmethod
  def setUpClass(cls):
      # print "setUpclass---->", parames
    cls.baseDriver=BaseDriver()
    cls.driver=cls.baseDriver.get_android_driver(parames)
    cls.get_element=GetByLocal(cls.driver)
    cls.main_business = MainPageBusiness(cls.driver)
    cls.login_business = LoginPageBusiness(cls.driver)

  def test_01_Case_cancel_update(self):
        print 1
        time.sleep(10)
        self.main_business.cancel_to_loginPage()
        time.sleep(2)
        # self.login_business.phone_login_success()
        # self.get_element.get_element("main_activity","nexttime").click()
        # time.sleep(1)
        # self.get_element.get_element("main_activity", "curriculum").click()
        # self.main_business.cancel_to_loginPage()
        # time.sleep(3)
        # self.driver.find_element_by_id('com.xinghuolive.live:id/tips_button')
        self.login_business.phone_login_success('18042460809', 'a5565473')
        # self.main_business.to_curriculumPage()
        # time.sleep(3)
        # self.main_business.to_loginPage()
        # time.sleep(3)
        # self.login_business.phone_login_success('18042460809', 'a5565473')
  def test_02_Case_to_login(self):
        print 2
        self.main_business.to_loginPage()
        time.sleep(3)

  def test_03_Case_phone_login_success(self):
        print 3
        self.login_business.phone_login_success('18042460809','a5565473')
        time.sleep(3)

def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_01_Case_cancel_update',parame=i))
    # suite.addTest(CaseTest('test_02_Case_to_login',parame=i))
    # suite.addTest(CaseTest('test_03_Case_phone_login_success', parame=i))
    html_file = "../report/report"+str(i)+".html"
    f = file(html_file, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(f)
    runner.run(suite)

if __name__ == '__main__':
    server=Server()
    server.main()
    time.sleep(10)
    device_list=server.get_device()
    process_list=[]
    for i in range(len(device_list)):
    # for i in range(1):
        print i
        process=multiprocessing.Process(target=get_suite,args=(i,))
        process_list.append(process)
    for j in process_list:
        j.start()
    # driver=BaseDriver().get_android_driver(0)
    # get_element = GetByLocal(driver)
    # time.sleep(20)
    # get_element.get_element("main_activity", "nexttime").click()
    # time.sleep(1)
    # get_element.get_element("main_activity", "to_login_btn").click()









