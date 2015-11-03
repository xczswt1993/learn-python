#-*- coding:utf-8 -*-
__author__ = 'stone'

import urllib
import urllib2

url = 'http://www.heibanke.com/lesson/crawler_ex00/'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
page = response.read().decode('utf-8')

print page

