"""
decorator test
https://qiita.com/makky05/items/1be6cf0f1f238b5ba01b
"""


funcs = []
def appender(*args, **kwargs):
    def decorator(f):
        # args や kwargsの内容によって処理内容を変えたり変えなかったり
        print(args)
        if kwargs.get('option1'):
            print('option1 is True')

        # 元の関数をfuncsに追加
        funcs.append(f)
    return decorator


@appender('arg1', option1=True)
def hoge():
    print('hoge')

@appender('arg2', option2=False)
def fuga():
    print('fuga')


# 以下と等価
'''
def hoge():
    print('hoge')
appender('arg1', option1=True)(hoge)

def fuga():
    print('fuga')
appender('arg2', option2=False)(fuga)
'''


def main():
    for f in funcs:
        f()

if __name__ == "__main__":
    main()
