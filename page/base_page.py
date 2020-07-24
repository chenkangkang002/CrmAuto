'''
页面类基类
'''
import time

from selenium.webdriver.support.select import Select

from base_data import BASE_PATH


class BasePage():

    def __init__(self, driver):
        '''初始化，实例化浏览器驱动对象'''
        self.driver = driver
        self.url = 'http://192.168.1.44/crm/index.php?m=user&a=login'  # 定义url
        self.timeout = 5

    def open(self):
        '''
        打开url
        :return:
        '''
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.timeout)  # 设置隐式等待

    def find_element(self, loc):
        '''元素定位'''
        return self.driver.find_element(*loc)

    def close_browser(self):
        '''关闭浏览器和浏览器驱动'''
        self.driver.quit()

    def assert_result(self, loc):
        '''
        断言信息获取'
        :param loc: 元素定位信息
        :return: 断言文本信息
        '''
        ret = str(self.find_element(loc).text).strip()
        return ret

    def select_search(self, loc, value='name'):
        ''''''
        element = self.find_element(loc)
        select = Select(element)
        try:
            select.select_by_value(value)
        except:
            try:
                select.select_by_visible_text(value)
            except:
                select.select_by_index(value)

    def screenshot(self, func_name='crm_auto'):
        '''截图,传入一个参数，最好是当前的方法名'''
        # 获取时间
        star_time = time.strftime('%Y%m%d_%H%M%S')
        func_name = func_name+'-'+star_time+'.png'
        self.driver.save_screenshot(BASE_PATH+'/report/'+func_name)