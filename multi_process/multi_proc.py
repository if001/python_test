"""
multi processのテスト
https://qiita.com/yotayokuto/items/23798d5fc75017d5a8b3
"""

from multiprocessing import Pool
from multiprocessing import Process


def function(hoge):
    print(hoge)
    x = 10
    return x


def multi(n):
    p = Pool(10) #最大プロセス数:10
    result = p.map(function, range(n))
    return result


def main():
    data = multi(20)
    for i in data:
        print(i)



if __name__ == "__main__":
   main()
