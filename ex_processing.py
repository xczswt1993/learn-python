#!/usr/bin/env python
from multiprocessing import Pool
from multiprocessing import Process
import os,time,random


def run_proc(name):
    print 'Run child process %s (%s)..' % (name,os.getpid())

def long_time_task(name):
    print 'Run task %s (%s)...' %(name,os.getpid())
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print 'task %s run %0.2f seconds.' %(name,(end-start))

if __name__ == '__main__':
    print 'parent process %s.' % os.getpid()
#    p = Process(target=run_proc,args=('test',))
#    print 'process will start'
#    p.start()
#    p.join()
#    print 'process end'
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print 'waiting for all subprocess done ...'
    p.close()
    p.join()
    print 'all subprocess done'

