from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page.base_page import BasePage


class AgSelectPage(BasePage):
    locator_agreement = (By.XPATH, "/html/body/div[1]/div/div/div[2]/ul[1]/li[7]/a")
    locator_keyword = (By.ID, 'search')
    locator_select = (By.XPATH, '//form[@id="searchForm"]/ul/li[4]/button')

    def agreement(self):
        '''点击合同'''
        self.driver.find_element(*self.locator_agreement).click()

    def ele_cli(self):
        '''点击下拉框并选择合同编号'''
        el = self.driver.find_element(By.ID, 'field')
        Select(el).select_by_value('number')

    def ele_cli2(self):
        '''点击下拉框并点击开始字符'''
        ele = self.driver.find_element(By.ID, 'condition')
        Select(ele).select_by_value('start_with')

    def ele_keyword(self, keyss):
        '''输入关键字'''
        self.driver.find_element(*self.locator_keyword).send_keys(keyss)

    def ele_select(self):
        '''点击搜索'''
        self.driver.find_element(*self.locator_select).click()

    def selectagreement(self, keyss):
        self.agreement()   # 点击合同
        self.ele_cli()      # 点击下拉框选择合同
        self.ele_cli2()     # 点击下拉框选择开始字符
        self.ele_keyword(keyss)      # 输入关键字
        self.ele_select()       # 点击搜索
        a = self.driver.current_url
        return a

