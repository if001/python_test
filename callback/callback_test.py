"""
https://qiita.com/moroku0519/items/315cd25d3eaae3217103

コールバック関数って？
コールバック関数とは、プログラム中で、呼び出し先の関数の実行中に実行されるように、あらかじめ指定しておく関数。
http://e-words.jp/w/%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AF%E9%96%A2%E6%95%B0.html
"""


def handler(func,*args):
    return func(*args)

def say_hello(name):
    print("Hello!!")
    print(name)


def function1(hoge):
    return hoge


def function2(hoge, huga):
    return hoge, huga



if __name__ == "__main__":
    callback = say_hello
    #callbackにsay_helloのオブジェクトIDを格納
    handler(callback, "moroku0519")


    handler(say_hello,"hello!!!!!!")


