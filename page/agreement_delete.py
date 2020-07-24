from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from page.base_page import BasePage

class AgDeletePage(BasePage):
    locator_agreement = (By.XPATH, "/html/body/div[1]/div/div/div[2]/ul[1]/li[7]/a")
    locator_xia1 = (By.ID, 'field')
    locator_xia2 = (By.ID, 'condition')
    locator_keyword = (By.ID, 'search')
    locator_select = (By.XPATH, '//form[@id="searchForm"]/ul/li[4]/button')
    locator_delete = (By.ID, 'delete')
    locator_assert = (By.CLASS_NAME, 'close')
    def agreement(self):
        '''点击合同'''
        self.driver.find_element(*self.locator_agreement).click()

    def ele_xiala1(self):
        '''点击下拉框并选择合同编号'''
        e = self.driver.find_element(*self.locator_xia1)
        Select(e).select_by_value('number')

    def ele_xiala2(self):
        '''点击下拉框并点击开始字符'''
        el = self.driver.find_element(*self.locator_xia2)
        Select(el).select_by_value('start_with')

    def ele_keyword(self, key):
        '''输入关键字'''
        self.driver.find_element(*self.locator_keyword).send_keys(key)

    def ele_select(self):
        '''点击搜索'''
        self.driver.find_element(*self.locator_select).click()

    def ele_click(self):
        '''点击第一个'''
        self.driver.find_elements_by_class_name("check_list")[1].click()

    def ele_delete(self):
        '''点击删除'''
        self.driver.find_element(*self.locator_delete).click()

    def ele_alert(self):
        '''获取alert上的文本并点击确定'''
        self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()

    def delete_agreement(self, key):
        '''删除合同'''
        self.agreement()         #点击合同
        self.ele_xiala1()       #点击下拉框选择合同编号
        self.ele_xiala2()       #点击下拉框选择开始字符
        self.ele_keyword(key)   #输入关键字
        self.ele_select()       #点击搜索
        time.sleep(3)
        self.ele_click()        #点击第一个
        time.sleep(3)
        self.ele_delete()       #点击删除
        self.ele_alert()        #点击确定

        text = self.driver.find_element(*self.locator_assert).text    #获取提示框信息
        return text










