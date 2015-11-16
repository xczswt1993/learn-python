#-*-coding:utf-8 -*-
def flib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n = n+1

flib(6)
def str2Int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'2':2,'3':3,'4':4}[s]
    return reduce(fn,map(char2num,s))
a = str2Int('23')
print a
def f(x):
    return x*x

map(f,[1,2,3,4,5,6,7,8,9])

l = []
for n in [1,2,3,4,5,6,7,8,9]:
    l.append(f(n))
print  l

map(str,[1,2,3,4,5,6,7,8,9])

def add(x,y):
    return x+y

reduce(add,[1,3,5,7,9])

def fn(x,y):
    return x*10+y
reduce(fn,[1,3,5,7,9])
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2Int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

def fun2(a):
    b = a[0].upper() + a[1:].lower()
    return b
z = map(fun2,x)
print z
