import unittest
from page.agreement_update import AgUpdate
from testcase.base_test import BaseTest

class ArUpdataTestCase(BaseTest):

    def test_edit_contract(self):
        '''修改合同'''
        self.assertEqual(self.admin,self.login_actual)
        p = AgUpdate(self.driver)
        p.update()

if __name__ == '__main__':
    unittest.main()
