from selenium.webdriver.common.by import By
from page.base_page import BasePage

class UpdateCluePage(BasePage):
    '''修改线索'''

    locator_clickupdate = (By.XPATH,'//form[@id="form1"]/table/tbody/tr/td[12]/a[3]')  # 修改
    locator_positin = (By.ID,'position')  # 职位
    locator_save = (By.CLASS_NAME,'btn.btn-primary')  # 保存
    locator_assert = (By.CLASS_NAME, 'alert.alert-success')  # 断言

    def ele_clickupdate(self):
        self.find_element(self.locator_clickupdate).click()  # 点击修改
        print("点击修改")

    def ele_positin(self,position):
        self.find_element(self.locator_positin).clear()  # 清空职位
        self.find_element(self.locator_positin).send_keys(position)  # 输入职位
        print("输入职位")

    def ele_save(self):
        self.find_element(self.locator_save).click()  # 点击保存
        print("点击保存")

    def ele_update(self,position):
        '''修改线索'''
        self.ele_clickupdate()
        self.ele_positin(position)
        self.ele_save()
        text = self.assert_result(self.locator_assert)
        return text
