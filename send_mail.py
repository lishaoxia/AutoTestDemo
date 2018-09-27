import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from  email.mime.multipart import MIMEBase

#发送邮箱服务器
smtpserver = 'smtp.exmail.qq.com'
#发送邮箱
sender = 'lichao@sdgakj.com'
#接收邮箱
receiver = 'lichao@sdgakj.com'
#发送邮箱用户、密码
user = 'lichao@sdgakj.com'
passwd = 'Lc2638581'

#  ============================定义发送邮件=================================
def send_mail(file_new):
    #获取测试报告内容，mail_body读取的是html代码，在第27行以html格式填充正文
    '''
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    '''
    #下面两行代码等价于上面的代码，优点：1、避免漏写关闭句柄 2、简单
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    #实例化一个邮件实体
    msg = MIMEMultipart()
    # MIMEText配置邮件正文内容，第一个参数为邮件正文，第二个文本格式，第三个utf-8编码
    msg.attach(MIMEText(mail_body,'html','utf-8'))


    #邮件附件1
    #设置附件的内容：读最新html的内容给附件,文本格式base64
    # att1 = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')与下面等价，上面with as 中定义了mail_body
    att1 = MIMEText(mail_body,'base64','utf-8')

    #application/octet-stream二进制流，不确定文件类型（任意文件类型）
    att1["Content-Type"] = 'application/octet-stream'

    #Content-disposition是 MIME 协议的扩展，如何显示附加的文件
    #attachment以附件的形式显示，可下载
    #filename写什么，邮件中附件名就是什么，不可写中文，不然发送的邮件中没有附件
    att1["Content-Disposition"] = 'attachment;filename="report.html"'
    msg.attach(att1)


    #邮件中显示发件人、接收人、主题
    msg['From'] = sender
    msg['To']  = receiver
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    #实例化smtplib模块的SMTP对象，连接并登录邮箱服务器,发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(user,passwd)
        smtp.sendmail(sender,receiver,msg.as_string())
    except smtplib.SMTPException:
        print("Error:无法发送邮件")


#  ================查找测试报告目录，找到最新生成的测试报告文件=================
def new_report(testreport):
    lists = os.listdir(testreport) #获取目录中的文件列表赋给lists
    # lamnda隐式函数，fn:...fn中间是函数,获取文件的最后修改时间，整行意思也就是根据文件的最后修改时间排序（ASC）
    lists.sort(key=lambda  fn:os.path.getmtime(testreport+'\\'+fn))
    file_new = os.path.join(testreport,lists[-1]) # 路径拼接，estreport\lastfile
    #print(file_new)
    return file_new