from page.addclue_page import AddCluePage
from page.switch_page import SwitchCluePage
from testcase.base_test import BaseTest

class ClueTestCase(BaseTest):
    def test_clue(self):
        '''添加线索转换为客户'''
        addclue = AddCluePage(self.driver)  # 实例化AddCluePage类
        contact = 'du先生'
        addclue.ele_addclue(contact)  # 调用AddCluePage的ele_clickclue方法
        switch = SwitchCluePage(self.driver)
        customer = '李白白白'
        text = switch.ele_switchclue(customer)  # 调用clue_page的ele_switchclue方法
        self.assertIn("添加客户成功", text)
