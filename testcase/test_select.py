import unittest
from page.agreement_select import AgSelect
from testcase.base_test import BaseTest

class ArSelectTestCase(BaseTest):

    def test_search_contract(self):
        '''搜索合同'''
        p = AgSelect(self.driver)
        p.select()

if __name__ == '__main__':
    unittest.main()
