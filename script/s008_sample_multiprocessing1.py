"""
    Process class : create a process object
    Parameter:
        target    : function name
        arg       : arg to function
    Functions:
        process.start()  : start process
        process.join()   : wait process finish
"""
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('Start download, The Process ID is [%d].' % getpid())
    print('Start download %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s Complete! Total of %d seconds' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('Total used of %.2f seconds.' % (end - start))
    
if __name__ == '__main__':
    main()

"""
Start download, The Process ID is [10192].
Start download Python从入门到住院.pdf...
Start download, The Process ID is [11300].
Start download Peking Hot.avi...
Python从入门到住院.pdf Complete! Total of 6 seconds
Peking Hot.avi Complete! Total of 8 seconds
Total used of 8.56 seconds.
"""