import fixtures
import time

#继承fixtures的Fixtures类
class ZtLogin(fixtures.Fixtures):
    """测试众测登录"""

    def test_login_usererror(self):
        '''用户名格式错误'''

        #调用父类的login()方法
        self.login('abcdefgh','123456')
        #assertEqual方法继承自父类的父类unittest.TestCase
        self.assertEqual(self.driver.find_element_by_css_selector('#err_login_email').text,'账号格式错误，请重新输入！')
        time.sleep(2)


    def test_login_usernotexsit(self):
        '''用户名不存在'''
        self.login('abcdef@163.com','123456')
        self.assertEqual(self.driver.find_element_by_css_selector('#err_login_email').text,'该账户不存在,请先注册账号')
        time.sleep(2)
