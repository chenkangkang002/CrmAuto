import time
import unittest
from model.driver import Driver
from page.login_page import LoginPage

class BaseTest(unittest.TestCase):

    def setUp(self):
        '''初始化浏览器对象'''
        print('初始化浏览器对象')
        self.driver = Driver().browser_chrome()
        login = LoginPage(self.driver)  # 实例化loginPage类
        u_name = 'admin'
        password = 'admin123'
        login_actual = login.login(u_name, password)  # 调用login page的login方法
        self.login_actual = login_actual
        self.admin = u_name

    def tearDown(self):
        '''清理'''
        time.sleep(3)
        print('关闭浏览器')
        self.driver.quit()

