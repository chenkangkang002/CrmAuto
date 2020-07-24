'''
创建客户测试用例
'''
from page.client_page import ClientPage
from page.login_page import LoginPage
from testcase.base_test import BaseTest


class ClientSearchTestCase(BaseTest):

    def test_client_search(self):
        '''查询客户'''
        #实例化登录page，先进行登录，再创建客户
        lp = LoginPage(self.driver)
        # file_path = r'E:\PyCharm2020(64bit)\py_workspace\crm_auto\data\data_text.txt'
        # data = get_txt(file_path, 2)  # [[],[]]模式获取用户名密码
        u_name = 'admin'
        password = 'admin123'
        actual = lp.login(u_name, password)  # 调用login page的login方法
        #实例化客户page
        cname = '李白白0001'
        value = 'name'
        cp = ClientPage(self.driver)
        cp.client_inlet()  # 点击导航栏入口
        ret_search = cp.search(cname,value) #查询
        self.assertEqual(cname, ret_search)

    def test_view_client(self):
        '''查看指定客户的详情信息'''
        cname = '陈晓晓'
        value = 'name'
        cp = ClientPage(self.driver)
        cp.client_inlet()
        cp.search(cname,value)
        ret = cp.view_client_info()
        cp.exit_system()
        self.assertEqual(cname, ret)