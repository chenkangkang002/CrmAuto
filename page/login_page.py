'''
登录page
'''
import time

from selenium.webdriver.common.by import By
from page.base_page import BasePage

class LoginPage(BasePage):

    #定位器
    login_username_text_loc = (By.NAME, 'name') #用户名定位器
    login_password_text_loc = (By.NAME, 'password') #登录密码定位器
    login_submit_loc = (By.NAME, 'submit') #登录按钮定位器
    login_assert = (By.XPATH,'//div[@class="container"]/div[2]/ul[2]/li[6]/a')    #断言定位器

    def login_username(self, uname):
        '''用户名输入框'''
        self.find_element(self.login_username_text_loc).click() #清理输入框
        self.find_element(self.login_username_text_loc).send_keys(uname)#输入用户名

    def login_password(self, passwd):
        '''密码输入框'''
        self.find_element(self.login_password_text_loc).click() #清理输入框
        self.find_element(self.login_password_text_loc).send_keys(passwd) #输入密码

    def login_submit(self):
        '''登录按钮'''
        self.find_element(self.login_submit_loc).click()    #点击【登录】

    def login(self, uname, passwd):
        '''登录操作'''
        self.open() #调用打开网站地址
        self.login_username(uname)  #调用输入用户名
        self.login_password(passwd) #调用输入密码
        self.login_submit() #调用点击【登录】
        time.sleep(2)
        ret = self.assert_result(self.login_assert)
        ret = ret.strip()
        self.screenshot('login')
        return ret