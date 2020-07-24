import unittest
from page.addclue_page import AddCluePage
from page.switch_page import SwitchCluePage
from testcase.base_test import BaseTest

class SwitchClueTestCase(BaseTest):

    def test_clue_client(self):
        '''线索转换为客户'''
        addclue = AddCluePage(self.driver)  # 实例化AddCluePage类
        addclue.ele_clickclue()  # 调用AddCluePage的ele_clickclue方法
        switch = SwitchCluePage(self.driver)  # 实例化SwitchCluePage
        customer = '李白白'
        text = switch.ele_switchclue(customer)  # 调用clue_page的ele_switchclue方法
        self.assertIn("添加客户成功", text)

if __name__ == '__main__':
    unittest.main()