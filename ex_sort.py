#-*- coding:utf-8 -*-
def reversed_cmp(x,y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

a = sorted([36,5,12,9,21],reversed_cmp)
print a

def cmp_inorge_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if(u1<u2):
        return -1
    if u1 > u2:
        return 1
    return 0

a = sorted(['bob','about','Zoo','Credit'],cmp_inorge_case)
print a

