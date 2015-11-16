#-*- coding:utf-8 -*-
__author__ = 'stone'

def is_odd(n):
    return n%2==1
a = filter(is_odd,[1,2,3,4,5,6,7,8])
print a

def not_empty(s):
    return s and s.strip()
a = filter(not_empty,['A','','B',None,'c',''])
print a
