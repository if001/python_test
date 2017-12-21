"""
multi processのテスト
https://corgi-lab.com/programming/python/python3-multi-thread/

threadインスタンスを生成
"""

import time
import threading
 
def proc():
    for i in range(0,5):
        time.sleep(1)
        print("count", i)
 
if __name__ == '__main__':
    th1 = threading.Thread(target=proc)
    th2 = threading.Thread(target=proc)
    th1.start()
    th2.start()
