import unittest
from data.data_lib import get_txt
from model import driver
from page.agreement_select import AgSelectPage
from page.login_page import LoginPage
from testcase.base_test import BaseTest


class ArSelectTestCase(BaseTest):
    def test_add(self):
        '''搜索合同'''
        login = LoginPage(self.driver)  # 实例化loginPage类
        file_path = r'C:\crm_auto\data\data_text.txt'
        data = get_txt(file_path, 2)  # [[],[]]模式获取用户名密码
        u_name = data[0][0]
        password = data[0][1]
        login.login(u_name, password)  # 调用login page的login方法

        p = AgSelectPage(self.driver)
        keyss = "5k"
        p.selectagreement(keyss)
        d = self.driver.current_url
        self.assertIn(keyss, d)


if __name__ == '__main__':
    unittest.main()
