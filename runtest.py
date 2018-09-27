import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from send_mail import new_report,send_mail


if __name__ == '__main__':
    #定义测试报告路径
    path = 'report'
    #定义测试用例根目录
    test_dir = 'case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    #获取当前时间并格式化
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    #测试报告命名
    reportname = path + '\\' + 'report_' + now + '.html'
    #打开测试报告文件，没有会自动创建一个
    fp = open(reportname,'wb')
    #执行测试
    runner = HTMLTestRunner(stream=fp,title='众测登录测试报告',description='用例执行情况')
    runner.run(discover)
    #关闭报告文件
    fp.close()

    #获取最新测试报告
    new_report = new_report(path)
    #发送邮件
    send_mail(new_report)

