# -*- coding:utf-8 -*-
__author__ = 'stone'
import smtplib
from email import  encoders
from email.header import  Header
from email.utils import parseaddr,formataddr
from email.mime.text import MIMEText

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr = ''
passwd = ''
to_addr = ''
smtp_server = 'smtp.qq.com'

msg = MIMEText('HELLO,SEND BY PYTHON ...','plain','utf-8')
msg['From'] = _format_addr(u'python <%s>' % from_addr)
msg['To'] = _format_addr(u'guanli <%s>' % to_addr)
msg['Subject'] = Header(u'from SMTP ...','utf-8').encode()

server = smtplib.SMTP(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,passwd)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
