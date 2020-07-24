import unittest

from page.addclue_page import AddCluePage
from page.login_page import LoginPage
from page.switch_page import SwitchCluePage
from testcase.base_test import BaseTest

class SwitchClueTestCase(BaseTest):
    def test_clue(self):
        '''线索转换为客户'''
        login = LoginPage(self.driver)  # 实例化LoginPage类
        u_name = 'admin'
        password = 'admin123'
        login.login(u_name, password)  # 调用login page的login方法
        addclue = AddCluePage(self.driver)  # 实例化AddCluePage类
        addclue.ele_clickclue()  # 调用AddCluePage的ele_clickclue方法
        switch = SwitchCluePage(self.driver)
        customer = '李白白'
        text = switch.ele_switchclue(customer)  # 调用clue_page的ele_switchclue方法
        self.assertIn("添加客户成功", text)
if __name__ == '__main__':
    unittest.main()