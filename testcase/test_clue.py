import unittest

from page.addclue_page import AddCluePage
from page.login_page import LoginPage
from page.switch_page import SwitchCluePage
from page.updateclue_page import UpdateCluePage
from testcase.base_test import BaseTest

class ClueTestCase(BaseTest):
    def test_clue(self):
        '''添加线索并修改并转换为客户'''
        login = LoginPage(self.driver)  # 实例化LoginPage类
        u_name = 'admin'
        password = 'admin123'
        login.login(u_name, password)  # 调用login page的login方法

        addclue = AddCluePage(self.driver)  # 实例化AddCluePage类
        contact = 'du先生'
        addclue.ele_addclue(contact)  # 调用AddCluePage的ele_clickclue方法

        update = UpdateCluePage(self.driver)  # 实例化UpdateCluePage
        position = 'HR'
        update.ele_update(position)  # 调用UpdateCluePage的ele_update方法

        switch = SwitchCluePage(self.driver)  # 实例化SwitchCluePage
        customer = '李白白白'
        text = switch.ele_switchclue(customer)  # 调用clue_page的ele_switchclue方法
        self.assertIn("添加客户成功", text)  # 断言
if __name__ == '__main__':
    unittest.main()