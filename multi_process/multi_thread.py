"""
multi processのテスト
https://corgi-lab.com/programming/python/python3-multi-thread/

threadクラスの継承
"""


import time
import threading
 
class myThread(threading.Thread):
    def __init__(self):
        super(myThread, self).__init__()
 
    def run(self):
        for i in range(0,5):
            time.sleep(1)
            print("count", i)
 
if __name__ == '__main__':
    th1 = myThread();
    th2 = myThread();
    th1.start()
    th2.start()
