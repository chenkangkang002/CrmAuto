import unittest
from data.data_lib import get_txt
from page.agreement_delete import AgDelete
from page.login_page import LoginPage
from testcase.base_test import BaseTest


class ArDeleteTestCase(BaseTest):
    def test_add(self):
        '''删除合同'''
        login = LoginPage(self.driver)  # 实例化loginPage类
        file_path = r'C:\crm_auto\data\data_text.txt'
        data = get_txt(file_path, 2)  # [[],[]]模式获取用户名密码
        u_name = data[0][0]
        password = data[0][1]
        actual = login.login(u_name, password)  # 调用login page的login方法
        self.assertEqual(u_name, actual)
        p = AgDelete(self.driver)
        p.delete()

        # self.assertEqual(actual, result)

if __name__ == '__main__':
    unittest.main()
