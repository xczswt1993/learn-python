#-*-coding:utf-8 -*-

import string,urllib2

def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        sName = string.zfill(i,5) + '.html'
        print '正在下载第' + str(i) +'个网页，并将其存储为'+sName+'...'
        f = open(sName,'w+')
        m = urllib2.urlopen(url+str(i)).read()
        f.write(m)
        f.close()
bdurl = 'http://tieba.baidu.com/p/4156758767'
end_page = 2
begin_page=1
baidu_tieba(bdurl,begin_page,end_page)

