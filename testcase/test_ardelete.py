import unittest
import time
from data.data_lib import get_txt
from page.agreement_delete import AgDeletePage
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
        login.login(u_name, password)  # 调用login page的login方法

        p = AgDeletePage(self.driver)     #实例化AgDeletePage类
        key = "00"
        time.sleep(3)
        text = p.delete_agreement(key)             #调用方法

        self.assertIn("×", text)    #断言


if __name__ == '__main__':
    unittest.main()
