'''
浏览器驱动
'''
from selenium import webdriver

class Driver():

    def browser_chrome(self):
        '''
        实例化Chrome
        :return: chrome浏览器对象driver
        '''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver