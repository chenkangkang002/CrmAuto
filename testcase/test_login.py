from testcase.base_test import BaseTest


class LoginTestCase(BaseTest):

    def test_loginfont_suss(self):
        '''测试前台登录成功'''
        self.assertEqual(self.admin, self.login_actual) #登录断言

