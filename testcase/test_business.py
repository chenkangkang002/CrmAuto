from page.business_page import BusinessPage
from testcase import base_test

class BusinessTestCase(base_test.BaseTest):

    def test_business_add(self):
        '''添加商机流程'''
        bname = 'dqfqdqw'
        busy = BusinessPage(self.driver)
        busy.home_business()
        busy.add_business()
        busy.business_add_flow(0,bname,'140')
        ret = busy.search_business(bname)
        self.assertEqual(bname, ret)

    def test_business_aedit(self):
        '''编辑商机'''
        bname = 'lily0004'
        busy = BusinessPage(self.driver)
        busy.home_business()
        busy.edit_business()
        busy.business_edit_flow(0, bname, '233')
        ret = busy.search_business(bname)
        self.assertEqual(bname, ret)

    def test_business_asearch(self):
        '''搜索商机'''
        bname = '李'
        busy = BusinessPage(self.driver)
        busy.home_business()
        # busy.business_search_flow('name','contains','')
        ret = busy.search_business(bname)
        self.assertEqual(bname, ret)

    def test_all_business_delete(self):
        '''删除全部商机'''
        busy = BusinessPage(self.driver)
        busy.home_business()
        busy.delete_business_all()
        # ret = busy.search_business(bname)
        self.assertEqual('1', '1')

    def test_part_business_delete(self):
        '''选择删除商机'''
        busy = BusinessPage(self.driver)
        busy.home_business()
        busy.delete_business_sel(0)
        self.assertEqual('1', '1')

