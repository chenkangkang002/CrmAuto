'''
新建线索-转化为客户的同时创建商机
'''
from page.business_page import BusinessPage
from page.client_page import ClientPage
from page.switch_page import SwitchCluePage
from testcase.base_test import BaseTest

class ClueClientBusiness(BaseTest):

    def test_clue_client_busniess1(self):
        '''新建线索，转化为客户——同时创建商机'''
        #添加线索
        contact = 'du先生008'
        addclue = SwitchCluePage(self.driver)  # 实例化AddCluePage
        text = addclue.ele_addclue(contact)  # 实例化AddCluePage的ele_addclue方法
        #线索转换-点击转换
        addclue.ele_switch()
        # 实例化客户page
        cname = '王八十0001'
        d_name = 'admin'
        bname = 'lily009'
        cp = ClientPage(self.driver)
        cp.client_not_ret(cname, d_name, sj='1')
        busy = BusinessPage(self.driver)
        busy.business_edit_flow(0, bname, '233002')
        ret = busy.search_business(bname)
        self.assertEqual(bname, ret)
