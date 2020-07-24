'''
新建客户的同时创建商机
'''
from page.business_page import BusinessPage
from page.client_page import ClientPage
from page.login_page import LoginPage
from testcase.base_test import BaseTest


class ClientAndBusiness(BaseTest):

    def test_client_busniess1(self):
        '''新建客户——同时创建商机'''
        lp = LoginPage(self.driver)
        u_name = 'admin'
        password = 'admin123'
        retlogin = lp.login(u_name, password)
        # 实例化客户page
        cname = '王jiu九'
        value = 'name'
        d_name = 'admin'
        bname = '2e2e2e20001'
        cp = ClientPage(self.driver)
        cp.client_inlet()  # 点击导航栏入口
        cp.create_client_butt()
        cp.client_not_ret(cname, d_name, sj='1')
        busy = BusinessPage(self.driver)
        busy.business_edit_flow(0, bname, '233001')

    def test_client_busniess2(self):
        '''新建客户——同时创建商机'''
        lp = LoginPage(self.driver)
        u_name = 'admin'
        password = 'admin123'
        retlogin = lp.login(u_name, password)
        # 实例化客户page
        cname = '王八0001'
        value = 'name'
        d_name = 'admin'
        bname = 'wd2e2e0001'
        cp = ClientPage(self.driver)
        cp.client_inlet()  # 点击导航栏入口
        cp.create_client_butt()
        cp.client_not_ret(cname, d_name, sj='1')
        busy = BusinessPage(self.driver)
        busy.business_edit_flow(0, bname, '233001')