import time
import unittest
from page.addclue_page import AddCluePage
from testcase.base_test import BaseTest

class ClueTestCase(BaseTest):
    def test_clue(self):
        '''添加线索'''
        contact = 'du先生三十四'
        addclue = AddCluePage(self.driver)  # 实例化AddCluePage
        time.sleep(3)
        text = addclue.ele_addclue(contact)  # 实例化AddCluePage的ele_addclue方法
        self.assertIn("线索添加成功", text)
if __name__ == '__main__':
    unittest.main()