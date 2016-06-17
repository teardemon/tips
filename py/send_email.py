#!/usr/bin/env python
# coding:utf8
import smtplib
import sys
import email.MIMEMultipart
import email.MIMEText
import email.MIMEBase

class send:
    def __init__(self,email_from,email_from_passwd,smtp_server,send_to):
        self.email_from = email_from
        self.email_from_passwd = email_from_passwd
        self.smtp_server = smtp_server
        self.send_to = send_to
    def send_email(self,title,content):
        server = smtplib.SMTP(self.smtp_server)
        server.login(self.email_from, self.email_from_passwd)
        # 构造MIMEMultipart对象做为根容器
        main_msg = email.MIMEMultipart.MIMEMultipart()
        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        text_msg = email.MIMEText.MIMEText(content,'plain','utf-8')
        main_msg.attach(text_msg) 
        # 设置根容器属性
        main_msg['From'] = self.email_from
        main_msg['To'] = self.send_to
        main_msg['Subject'] = title
        main_msg['Date'] = email.Utils.formatdate()
        # 得到格式化后的完整文本
        fullText = main_msg.as_string( )
        # 用smtp发送邮件
        try:
            server.sendmail(self.email_from, self.send_to, fullText)
        finally:
            server.quit()

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print 'Usage:%s title content'% sys.argv[0]
        sys.exit(2)
    else:
        s1 = send('xxxx@qq.com','xxxx','smtp.qq.com','xxx@163.com')
        s1.send_email(sys.argv[1],sys.argv[2])
