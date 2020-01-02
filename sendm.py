# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

import psutil

mail_host = "smtp.163.com"      # SMTP服务器
mail_user = "yyangchow@163.com" # 用户名
mail_pass = "Hf41845367"        # 授权密码，非登录密码

sender = "yyangchow@163.com"
receivers = ['zhou940521@163.com','a05211024@163.com']

total, used, free, percent = psutil.disk_usage('/')
msg_str = "\t硬盘总共{0}G,已经使用{1}G, {3}%, 剩余{2}G!".format(round(total/1024**3, 2), round(used/1024**3, 2), round(free/1024**3, 2), percent)

name, addr = parseaddr("Ubuntu系统管理员<%s>" % sender)
fromadr = formataddr((Header(name, 'utf-8').encode(),addr))

subject = "系统硬盘监控"
message = MIMEText(msg_str, 'plain', 'utf-8')
message['From'] = fromadr
message['To'] = ','.join(receivers)
message['Subject'] = Header(subject, 'utf-8')

if __name__ == "__main__":
    server = smtplib.SMTP_SSL(mail_host, 465)
    server.login(mail_user,mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    server.close()

