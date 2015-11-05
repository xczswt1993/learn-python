#-*- coding:utf-8 -*-
__author__ = 'stone'

import urllib
import urllib2
import  re
url = 'http://www.heibanke.com/lesson/crawler_ex00/'

#r'数字(.*?)</h3>' 第一页数字
#  r'数字是(.*?)\.' 之后的数字

def search_num(pattern,url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    result = re.search(pattern,page)
    if result is not None:
            num = result.group(1)
            return num
    else:
        return None

pattern1 = r'数字(.*?)</h3>'
nextNum = search_num(pattern1,url)
pattern2 = r'数字是(.*?)\.'
while True:
    nextUrl = url + str(nextNum)
    nextNum = search_num(pattern2,nextUrl)
    if nextNum is not None:
        print 'nextNum:',nextNum
    else:
        print u'完成！'
        break


