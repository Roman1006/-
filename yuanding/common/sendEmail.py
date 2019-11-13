#该文件是构造发送邮件的方法，用到python标准库smtplib和email
#可以获取最新的测试报告，把最新的测试报告以文本和附件的形式发送
import smtplib
import os
from common.myLog import MyLog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.readConfig import ReadConfig

# 路径
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
reportpath = path_dir + '/report'

local_readConfig = ReadConfig()


class SendEmail:
    def __init__(self):
        global host, user, password, sender, title
        host = local_readConfig.get_email('mail_host')  # 邮箱服务器
        user = local_readConfig.get_email('mail_user')  # 发件人用户名
        password = local_readConfig.get_email('mail_pass')  # 发件人邮箱授权码，非登录密码
        sender = local_readConfig.get_email('sender')  # 发件人邮箱
        title = local_readConfig.get_email('title')  # 邮件标题
        self.logger = MyLog()
        self.receive_user = local_readConfig.get_email('receive_user')  # 收件人邮箱
        self.receive_user_list = []
        for i in str(self.receive_user).split('/'):
            self.receive_user_list.append(i)

    def send_email(self):
        """把最新的测试报告以邮件的方式发送"""
        # 构造邮件
        file_new = self.get_new_report()
        f = open(file_new, 'rb')
        content = f.read()
        message = MIMEMultipart()
        message['From'] = "{}".format(sender)  # 发件人
        message['To'] = ",".join(self.receive_user_list)  # 收件人
        message['Subject'] = Header(title, 'utf-8')  # 标题
        message.attach(MIMEText(content, 'html', 'utf-8'))

        # 添加附件
        filename = file_new[-31:]
        att = MIMEText(content, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=%s' % filename
        message.attach(att)

        # 发送邮件
        try:
            server = smtplib.SMTP()
            server.connect(host)
            server.login(user, password)  # 登录验证
            server.sendmail(sender, self.receive_user_list, message.as_string())  # 发送
            server.quit()  # 关闭
            self.logger.info("邮件发送成功！")
        except smtplib.SMTPException as e:
            # print("邮件发送失败！")
            self.logger.error("邮件发送失败！请检查邮件配置%s" % e)

    def get_new_report(self):
        """获取最新的测试报告"""
        lists = os.listdir(reportpath)
        if lists:
            lists.sort(key=lambda fn: os.path.getmtime(reportpath + '\\' + fn))
            file_new = os.path.join(reportpath, lists[-1])
            return file_new
