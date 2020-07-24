import unittest
from page.agreement_add import AgAdd
from testcase.base_test import BaseTest

class ArAddTestCase(BaseTest):

    def test_add(self):
        '''添加合同'''
        self.assertEqual(self.admin, self.login_actual)
        p = AgAdd(self.driver)
        p.add()

if __name__ == '__main__':
    unittest.main()
