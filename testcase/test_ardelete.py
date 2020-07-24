import unittest
from page.agreement_delete import AgDelete
from testcase.base_test import BaseTest

class ArDeleteTestCase(BaseTest):
    def test_delete_contract(self):
        '''删除合同'''
        self.assertEqual(self.admin, self.login_actual)
        p = AgDelete(self.driver)
        p.delete()

if __name__ == '__main__':
    unittest.main()
