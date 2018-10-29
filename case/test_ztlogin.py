import fixtures
import time,os,csv
from itertools import islice

#获取工程所在目录
root_dir = os.getcwd() #获取当前运行文件的目录 runtest.py运行时，调用改文件的此方法，所以获取的是runtest.py文件的目录
screenpath = os.path.join(root_dir,'screenshot')


#继承fixtures的Fixtures类
class ZtLogin(fixtures.Fixtures):
    """测试众测登录"""
    def test_login_usererror(self):
        '''用户名格式错误'''
        user_data_csv = os.path.join(root_dir,'data','user_data.csv')   #定义测试数据文件目录
        user_data = csv.reader(open(user_data_csv,'r'))     #读取测试数据
        for (username,password) in islice(user_data,1,None):    #切片去掉测试数据第一行。行数从0开始，（f,m,n）取第m 到 n-1行
            try:    #还用try ... except ...防止抛出异常程序停止运行
                #调用父类的login()方法
                self.login(username,password)   #测试数据参数化
                #assertEqual方法继承自父类的父类unittest.TestCase
                self.assertEqual(self.driver.find_element_by_css_selector('#err_login_email').text,'账号格式错误，请重新输入！')
                #self.driver.save_screenshot( )
                #self.driver.get_screenshot_as_base64()
                now = time.strftime('%Y-%m-%d %H_%M_%S')
                screenname = os.path.join( screenpath,'test_login_usererror_' +  now + ".jpg")
                self.driver.get_screenshot_as_file(screenname)  #截图
                time.sleep(1)
            except Exception as e:
                print("Exception:",e)

    def test_login_usernotexsit(self):
        '''用户名不存在'''
        try:
            self.login('abcdef@163.com','123456')
            self.assertEqual(self.driver.find_element_by_css_selector('#err_login_email').text,'该账户不存在,请先注册账号')
            time.sleep(2)
        except Exception as e:
            print("Exception:",e)
