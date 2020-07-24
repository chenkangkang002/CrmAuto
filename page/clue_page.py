from selenium.webdriver.common.by import By
from page.base_page import BasePage

class CluePage(BasePage):

    locator_clickclue = (By.LINK_TEXT, '线索')  # 线索
    locator_newcreate = (By.CSS_SELECTOR,'a.btn.btn-primary')  # 新建线索
    locator_contact = (By.CSS_SELECTOR,'input#contacts_name')  # 联系人姓名
    locator_save = (By.CSS_SELECTOR,'input.btn.btn-primary')  # 保存
    locator_switch = (By.LINK_TEXT, '转换')  # 转换
    locator_customername = (By.NAME,'name')  # 客户名称
    locator_html = (By.TAG_NAME,"html")  #窗口尺寸
    locator_switchsave = (By.XPATH,'//form[@id="form1"]/table/tfoot/tr/td/input[1]')  # 保存
    locator_assert = (By.CLASS_NAME, 'alert.alert-success')  # 断言

    def ele_clickclue(self):
        '''点击【线索】'''
        self.find_element(self.locator_clickclue).click()  # 点击【线索】
        print("点击线索")

    def ele_newcreate(self):
        '''点击新建线索'''
        self.find_element(self.locator_newcreate).click()  # 点击新建线索
        print("点击新建线索")

    def ele_contact(self,contact):
        '''输入联系人名称'''
        self.find_element(self.locator_contact).send_keys(contact)  # 输入联系人名称
        print("输入联系人名称")

    def ele_save(self):
        '''点击【保存】'''
        self.find_element(self.locator_save).click()  # 点击【保存】
        print("点击保存")

    def ele_switch(self):
        '''点击转换'''
        self.find_element(self.locator_switch).click()  # 点击转换
        print("点击转换")

    def ele_customername(self,customer):
        '''输入客户名称'''
        self.find_element(self.locator_customername).send_keys(customer)  # 输入客户名称
        print("输入客户名称")

    def ele_scroll(self):
        '''滚动窗口'''
        xy = self.find_element(self.locator_html).size
        js = "window.scroll(0,%s)" % (xy["height"])
        self.driver.execute_script(js)  # 滚动窗口
        print("窗口滚动")

    def ele_switchsave(self):
        '''点击保存'''
        self.find_element(self.locator_switchsave).click()  # 点击保存
        print("点击保存")

    def ele_clue(self,contact,customer):
        '''添加线索转换为客户'''
        self.ele_clickclue()
        self.ele_newcreate()
        self.ele_contact(contact)
        self.ele_save()
        self.ele_switch()
        self.ele_customername(customer)
        self.ele_scroll()
        self.ele_switchsave()
        text = self.assert_result(self.locator_assert)
        return text
