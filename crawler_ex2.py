# -*- coding:utf-8 -*-
__author__ = 'stone'

import  requests
import re
password = 0
url = 'http://www.heibanke.com/lesson/crawler_ex01/'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'}

form_data = {
    'username':'a',
    'password':password,
    'csrfmiddlewaretoken':"qiomOnPU4cI7R0hJMMOLDzJhvIRLyrVe"
}
while True:
    s = requests.post(url,data=form_data,headers = header)
    page = s.text
    pattern = u'密码错误'
    reg = re.search(pattern,page)
    result = reg.group(0)
    print 'result:',result,'password',password
    password = password +1



