#-*- coding:utf-8 -*-
__author__ = 'stone'

import urllib
import urllib2
import  re
url = 'http://www.heibanke.com/lesson/crawler_ex00/'

#r'数字(.*?)</h3>'
#

def search_num(pattern,url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    result = re.search(pattern,page)
    num = result.group(1)
    return num

pattern1 = r'数字(.*?)</h3>'
nextNum = search_num(pattern1,url)

pattern2 = r'数字是(.*?)\.'
while True:
    nextUrl = url + str(nextNum)
    nextNum = search_num(pattern2,nextUrl)
    print nextNum







