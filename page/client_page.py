'''
客户page
'''
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ClientPage(BasePage):

    #定位器
    loc_client_inlet = (By.LINK_TEXT, '客户') #客户功能入口
    loc_create_client = (By.CSS_SELECTOR,'a.btn.btn-primary' )  #创建客户入口按钮
    #创建客户页面
    loc_client_name = (By.NAME, 'name') #客户名称
    loc_create_business1 = (By.NAME, 'create_business1')    #同时创建商机单选框
    loc_preserve_submit = (By.XPATH, '//form[@id="form1"]/table/tfoot/tr/td/input[1]') #保存按钮
    loc_assert = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[3]/a/span')   #断言
    loc_search = (By.ID, 'search') #搜索输入框
    loc_dosearch = (By.ID, 'dosearch') #搜索按钮
    loc_search_condition = (By.ID, 'field') #筛选条件
    loc_search_result = (By.XPATH,'//table[@class="table table-hover table-striped table_thead_fixed"]/tbody/tr/td[3]/a/span') #查询返回结果（客户名称）
    #选择负责人
    loc_leading_cadre = (By.ID, 'owner_name')   #负责人
    loc_d_name = (By.ID, 'd_name')  #用户名（选择客户负责人）
    loc_leading_cadre_search = (By.XPATH, '//*[@id="dialog-role-list"]/div/ul/button')  #搜索（选择客户负责人）
    loc_owner_radio = (By.NAME, 'owner')    #负责人勾选框
    loc_leading_cadre_submit = (By.XPATH, '/html/body/div[7]/div[3]/div/button[1]/span') #ok按钮
    loc_view_client = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[1]') #查看客户
    loc_view_client_name = (By.XPATH, '//ul[@id="left_list"]/li[1]/span') #查看客户信息时的客户名称
    loc_head_scu = (By.CLASS_NAME, 'avatar') #右上角头像
    loc_exit_system = (By.LINK_TEXT, '退出') #退出系统

    def exit_submit(self):
        '''点击【退出】，退出系统'''
        self.find_element(self.loc_exit_system).click()

    def head_scu(self):
        '''点击右上角头像，弹出用户操作列表'''
        self.find_element(self.loc_head_scu).click()

    def view_client(self):
        '''点击【查看】，查看客户信息'''
        self.find_element(self.loc_view_client).click()

    def client_inlet(self):
        '''客户功能入口按钮'''
        self.find_element(self.loc_client_inlet).click()

    def create_client_butt(self):
        '''创建客户入口按钮'''
        self.find_element(self.loc_create_client).click()

    def leading_cadre(self):
        '''点击负责人'''
        self.find_element(self.loc_leading_cadre).click()

    def d_name(self, d_name='admin'):
        '''输入负责人用户名'''
        self.find_element(self.loc_d_name).clear()
        self.find_element(self.loc_d_name).send_keys(d_name)

    def leading_cadre_search(self):
        '''点击负责人搜索按钮'''
        self.find_element(self.loc_leading_cadre_search).click()

    def owner_radio(self):
        '''勾选负责人'''
        self.find_element(self.loc_owner_radio).click()

    def leading_cadre_submit(self):
        '''点击【OK】，确定负责人'''
        self.find_element(self.loc_leading_cadre_submit).click()

    def client_name(self, cname):
        '''客户名称输入框'''
        self.find_element(self.loc_client_name).clear()
        self.find_element(self.loc_client_name).send_keys(cname)

    def create_business1(self):
        '''同时创建商机'''
        self.find_element(self.loc_create_business1).click()

    def preserve_submit(self):
        '''保存按钮'''
        self.find_element(self.loc_preserve_submit).click()

    def search_condition(self, value='name'):
        '''筛选条件下拉框'''
        self.find_element(self.loc_search_condition).click()
        self.select_search(self.loc_search_condition, value)

    def search_input(self, cname):
        '''搜索输入框'''
        self.find_element(self.loc_search).clear()
        self.find_element(self.loc_search).send_keys(cname)

    def client_search_butt(self):
        '''搜索按钮'''
        self.find_element(self.loc_dosearch).click()

    def client(self, cname, d_name,sj='0'):
        '''创建客户功能实现,有返回值，传入参数：cname客户名，sj是否创建商机默认sj='0' 不创建'''
        self.client_name(cname)
        self.choose_leading_cadre(d_name)
        if sj == '0':
            pass
        else:
            self.create_business1()
        self.preserve_submit()
        ret = self.assert_result(self.loc_assert)
        return ret

    def client_not_ret(self, cname, d_name,sj='0'):
        '''创建客户功能实现,无返回值，传入参数：cname客户名，sj是否创建商机默认sj='0' 不创建'''
        self.client_name(cname)
        self.choose_leading_cadre(d_name)
        if sj == '0':
            pass
        else:
            self.create_business1()
        self.preserve_submit()

    def search(self, cname, value):
        '''实现客户名称搜索,并返回结果，输入参数：cname客户名，value下拉选项的value默认为value=“name”'''
        self.search_condition(value)
        self.search_input(cname)
        self.client_search_butt()
        time.sleep(2)
        ret = self.assert_result(self.loc_search_result)
        return ret

    def choose_leading_cadre(self, d_name):
        '''在弹出页面中选择负责人'''
        self.leading_cadre()
        self.d_name(d_name)
        self.leading_cadre_search()
        self.owner_radio()
        self.leading_cadre_submit()

    def view_client_info(self):
        '''查看客户信息'''
        self.view_client()
        ret = self.assert_result(self.loc_view_client_name)
        self.screenshot('view_client_info')
        return ret

    def exit_system(self):
        '''点击右上角头像，退出系统'''
        self.head_scu()
        self.exit_submit()
        self.screenshot('exit_system')