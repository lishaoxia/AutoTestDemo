import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import time



#创建测试类，继承unittest下的TestCase类
class TstZtlogin(unittest.TestCase):
    """测试众测登录"""
    def setUp(self):
        '''self 相当于Java中的this,代表类实例本身，这样self.driver就可以被类中的其他函数使用，不使用self 的话driver只是一
        个setUp函数的局部变量'''
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.ztestin.com')
        self.driver.find_element_by_css_selector('#qqww > div.zheader > div > ul > li.nav_function > a').click()

    def test_login_usererror(self):
        '''用户名格式错误'''
        self.driver.find_element_by_css_selector('#login_email').clear()
        self.driver.find_element_by_css_selector('#login_email').send_keys('abcdefg')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#login_password').clear()
        self.driver.find_element_by_css_selector('#login_password').send_keys('123456')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btn_submit1989 > button').click()
        self.assertEqual(self.driver.find_element_by_css_selector('#err_login_email').text,'账号格式错误，请重新输入！')
        time.sleep(2)

    def test_login_usernotexsit(self):
        '''用户名不存在'''
        self.driver.find_element_by_css_selector('#login_email').clear()
        self.driver.find_element_by_css_selector('#login_email').send_keys('abcdefg@163.com')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#login_password').clear()
        self.driver.find_element_by_css_selector('#login_password').send_keys('123456')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btn_submit1989 > button').click()
        self.assertEqual(self.driver.find_element_by_css_selector('#err_login_email').text,'该账户不存在,请先注册账号')
        time.sleep(2)
    #最后调用tearDown()函数，与函数所在位置无关

    def tearDown(self):
        self.driver.close()

#比如Java类中main（）函数，有main()函数才能直接执行
if __name__ == '__main__':
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TstZtlogin("test_login_usererror"))
    suite.addTest(TstZtlogin("test_login_usernotexsit"))
    #定义测试报告的路径
    path = 'report'
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    reportname = path +'\\'+'report_'+ now + '.html'
    fp = open(reportname,'wb')
    #执行测试
    runner = HTMLTestRunner(stream=fp,title='众测登录测试报告',description='用例执行情况')
    runner.run(suite)
    #关闭报告文件
    fp.close()
