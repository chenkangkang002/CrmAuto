import unittest

from page.addclue_page import AddCluePage
from page.login_page import LoginPage
from page.updateclue_page import UpdateCluePage
from testcase.base_test import BaseTest

class UpdateClueTestCase(BaseTest):
    def test_clue(self):
        '''修改线索'''

        addclue = AddCluePage(self.driver)  # 实例化AddCluePage类
        addclue.ele_clickclue()  # 调用AddCluePage的ele_clickclue方法

        update = UpdateCluePage(self.driver)  # 实例化UpdateCluePage
        position = '人事'
        text = update.ele_update(position)  # 调用UpdateCluePage的ele_update方法
        self.assertIn("线索修改成功！", text)
if __name__ == '__main__':
    unittest.main()