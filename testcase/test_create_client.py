'''
创建客户测试用例
'''
from page.client_page import ClientPage
from testcase.base_test import BaseTest

class CreateClientTestCase(BaseTest):

    def test_create_client(self):
        '''创建客户'''
        #实例化客户page
        cname = '王八0001'
        value = 'name'
        d_name = 'admin'
        cp = ClientPage(self.driver)
        cp.client_inlet()  # 点击导航栏入口
        cp.create_client_butt()
        cp.client_not_ret(cname, d_name)
        ret_search = cp.search(cname,value) #查询
        print(ret_search)
        self.assertEqual(cname, ret_search)