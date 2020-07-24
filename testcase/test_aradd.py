import unittest

from data.data_lib import get_txt
from page.agreement_add import AgAddPage
from page.login_page import LoginPage
from testcase.base_test import BaseTest


class ArAddTestCase(BaseTest):
    def test_add(self):
        '''添加合同'''
        login = LoginPage(self.driver)  # 实例化loginPage类
        file_path = r'C:\crm_auto\data\data_text.txt'
        data = get_txt(file_path, 2)  # [[],[]]模式获取用户名密码
        u_name = data[0][0]
        password = data[0][1]
        login.login(u_name, password)  # 调用login page的login方法

        p = AgAddPage(self.driver)   #实例化AgAdd
        nu = "0000001"
        uname = "admin"
        text = p.add_agreement(nu, uname)     #调用AgAdd中的add方法

        self.assertIn("×", text)     #断言


if __name__ == '__main__':
    unittest.main()
