'''商机页面'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page.base_page import BasePage


class BusinessPage(BasePage):
    #定位器
    locator_home_business = (By.XPATH, '//div[@class="container"]/div[2]/ul[1]/li[3]/a')
    locator_add_business = (By.XPATH,'//div[@class="row"]/div[1]/div/a')
    locator_customer_name = (By.ID,'customer_name')
    locator_customer = (By.NAME,'customer')
    locator_confirm_add_cus = (By.CSS_SELECTOR,'div[id="dialog-message"]+div>div button:nth-child(1)>span')
    locator_business_name = (By.ID,'name')
    locator_business_price = (By.ID,'estimate_price')
    locator_confirm_business = (By.XPATH,'//form[@id="form1"]/table/tfoot/tr/td/input[1]')
    locator_edit_business = (By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[3]')
    locator_confirm_edit_business = (By.XPATH,'//div[@class="container"]/div[2]/div/form/table/tfoot/tr/td/input[1]')
    locator_select_field = (By.ID,'field')
    locator_select_condition = (By.ID, 'condition')
    locator_search_key = (By.ID, 'search')
    locator_search_button = (By.ID, 'dosearch')
    locator_delete_all= (By.ID,'check_all')
    locator_delete_button = (By.ID,'delete')
    #搜索
    loc_search = (By.ID, 'search')  # 搜索输入框//*[@id="form1"]/table/tbody/tr[1]/td[4]/a/span
    loc_dosearch = (By.ID, 'dosearch')  # 搜索按钮
    loc_search_condition = (By.ID, 'field')  # 筛选条件
    loc_search_result = (By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[4]/a/span')  # 查询返回结果（商机名称）
    locator_view_business = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[1]')
    locator_back_view_business = (By.XPATH, '//div[@id="tab1"]/div[1]/div/a[3]')

    def loc_search_input(self, bname):
        '''搜索输入框'''
        self.find_element(self.loc_search).clear()
        self.find_element(self.loc_search).send_keys(bname)

    def loc_search_condition_sel(self):
        '''筛选条件'''
        self.find_element(self.loc_search_condition).click()
        self.select_search(self.loc_search_condition)

    def  loc_dosearch_butt(self):
        '''搜索按钮'''
        self.find_element(self.loc_dosearch).click()

    def loc_search_assert_result(self):
        '''搜索断言'''
        ret = self.assert_result(self.loc_search_result)
        return ret

    def home_business(self):
        '''点击商机进入'''
        action = self.find_element(self.locator_home_business)
        action.click()

    def add_business(self):
        '''点击添加商机'''
        action = self.find_element(self.locator_add_business)
        action.click()

    def create_business_cusname(self):
        '''添加客户名称，跳转至选择客户'''
        action = self.find_element(self.locator_customer_name)
        action.click()

    def select_customer(self,index):
        '''选择客户'''
        self.driver.find_elements(*self.locator_customer)[index].click()

    def add_customer(self):
        '''确认添加客户'''
        action = self.find_element(self.locator_confirm_add_cus)
        action.click()

    def business_add_name(self,bname):
        '''输入商机名'''
        action = self.find_element(self.locator_business_name)
        action.clear()
        action.send_keys(bname)

    def business_price(self,price):
        '''输入商机金额'''
        action = self.find_element(self.locator_business_price)
        action.clear()
        action.send_keys(price)

    def confirm_business(self):
        '''点击确认'''
        action = self.find_element(self.locator_confirm_business)
        action.click()

    def edit_business(self):
        '''点击编辑'''
        action = self.find_element(self.locator_edit_business)
        action.click()

    def business_edit_name(self,bname):
        '''输入商机名'''
        action = self.find_element(self.locator_business_name)
        # action.clear()
        # time.sleep(1)
        # self.driver.switch_to.alert.accept()
        action.send_keys(bname)

    def confirm_edit_business(self):
        '''点击确认编辑'''
        action = self.find_element(self.locator_confirm_edit_business)
        action.click()

    def search_business_fieid(self,value):
        '''选择筛选字段'''
        ele = self.find_element(self.locator_select_field)
        select = Select(ele)
        select.select_by_value(value)

    def search_business_condition(self,value):
        '''选择筛选条件'''
        ele = self.find_element(self.locator_select_condition)
        select = Select(ele)
        select.select_by_value(value)

    def search_business_key(self,key):
        '''输入关键字'''
        action = self.find_element(self.locator_search_key)
        action.clear()
        action.send_keys(key)

    def search_business_button(self):
        '''点击搜索'''
        action = self.find_element(self.locator_search_button)
        action.click()

    def delete_business(self,index):
        '''选择商机'''
        self.driver.find_elements(By.CLASS_NAME,'check_list')[index].click()

    def delete_all_business(self):
        '''全选商机'''
        action = self.find_element(self.locator_delete_all)
        action.click()

    def delete_button(self):
        '''点击删除按钮'''
        action = self.find_element(self.locator_delete_button)
        action.click()

    def confirm_delete(self):
        '''确认删除'''
        self.driver.switch_to.alert.accept()

    def click_view_business(self):
        '''点击查看商机'''
        action = self.find_element(self.locator_view_business)
        action.click()

    def back_view_business(self):
        '''查看商机返回'''
        action = self.find_element(self.locator_back_view_business)
        action.click()

    def business_add_flow(self,index,bname,price):
        '''添加商机流程'''
        self.create_business_cusname()
        time.sleep(1)
        self.select_customer(index)
        time.sleep(1)
        self.add_customer()
        time.sleep(1)
        self.business_add_name(bname)
        time.sleep(1)
        self.business_price(price)
        time.sleep(1)
        self.confirm_business()
        time.sleep(1)

    def business_edit_flow(self,index,bname,price):
        '''编辑商机流程'''
        self.create_business_cusname()
        time.sleep(1)
        self.select_customer(index)
        time.sleep(1)
        self.add_customer()
        time.sleep(1)
        self.business_edit_name(bname)
        time.sleep(1)
        self.business_price(price)
        time.sleep(1)
        self.confirm_edit_business()
        time.sleep(1)

    def business_search_flow(self,field,condition,key):
        '''搜索商机流程'''
        self.search_business_fieid(field)
        time.sleep(1)
        self.search_business_condition(condition)
        time.sleep(1)
        self.search_business_key(key)
        time.sleep(1)
        self.search_business_button()
        time.sleep(1)

    def delete_business_all(self):
        '''删除全部商机'''
        self.delete_all_business()
        self.delete_button()
        self.confirm_delete()

    def delete_business_sel(self,index):
        '''选择删除商机'''
        self.delete_business(index)
        time.sleep(1)
        self.delete_button()
        time.sleep(1)
        self.confirm_delete()
        time.sleep(1)

    def search_business(self, bname):
        '''通过商机名查询商机'''
        self.loc_search_condition_sel()
        self.loc_search_input(bname)
        self.loc_dosearch_butt()
        ret = self.loc_search_assert_result()
        return ret

    def view_business(self):
        '''查看商机'''
        self.click_view_business()
        time.sleep(1)
        self.back_view_business()
        time.sleep(1)
