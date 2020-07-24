'''
批量执行测试用例
'''
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
#筛选测试用例文件
discover = unittest.defaultTestLoader.discover(start_dir='testcase/',
                                    pattern='test_*.py',
                                    top_level_dir=None
                                    )
#获取时间
star_time = time.strftime('%Y%m%d_%H%M%S')
#设置报告文件名
filename = 'report-'+star_time+'.html'
#打开文件对象
with open('./report/'+filename,'wb+') as f:
    #实例化htmltestrunner对象
    runner = HTMLTestRunner(f,
                            title='Crm自动化测试',
                            description='自动化注册详细测试报告')
    runner.run(discover)
