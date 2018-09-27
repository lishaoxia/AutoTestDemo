import unittest
import time
from selenium import webdriver

#创建fixture类，继承unittest下的TestCase类，作用如下：
# 主要作用是对测试用例执行前环境的初始化和执行后环境的销毁的方法的封装
# 也可以将一些固定方法封装在此类中，比如下方的登录方法


"""unittest对模块、类、方法提供了3个范围的fixture,模块的fixture一个模块调用一次setUp和tearDown方法，类的fixture一个类
调用一次setUp和tearDown方法，方法的fixture一个方法调用一次setUp和tearDown方法"""

'''
模块fixture
def setUpModule():
    print("XXXXXXXX")
def tearDownModule():
    print("XXXXXXXX")
'''

class Fixtures(unittest.TestCase):
    """测试众测登录"""
    #类fixture,需要@classmethod修饰，cls与self没有什么特别之处，也是一种约定，可以替换成abc
    @classmethod
    def setUpClass(cls):
        '''self 相当于Java中的this,代表类实例本身，这样self.driver就可以被类中的其他函数使用，不使用self 的话driver只是一
        个setUp函数的局部变量'''
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get('https://www.ztestin.com')
        cls.driver.find_element_by_css_selector('#qqww > div.zheader > div > ul > li.nav_function > a').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    """
    #方法fixture
    #setUp()和setDown()函数会在unittest执行用例前后自动调用
    def setUp(self):
        '''self 相当于Java中的this,代表类实例本身，这样self.driver就可以被类中的其他函数使用，不使用self 的话driver只是一
        个setUp函数的局部变量'''
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.ztestin.com')
        self.driver.find_element_by_css_selector('#qqww > div.zheader > div > ul > li.nav_function > a').click()

    #最后调用tearDown()函数，与函数所在位置无关
    def tearDown(self):
        self.driver.close()
    """

    #定义登录函数
    def login(self,username,passwd):
        self.driver.find_element_by_css_selector('#login_email').clear()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#login_email').send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#login_password').clear()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#login_password').send_keys(passwd)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btn_submit1989 > button').click()

