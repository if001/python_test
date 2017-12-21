"""
decorator test
https://qiita.com/makky05/items/1be6cf0f1f238b5ba01b
"""


def args_joiner(*dargs, **dkwargs):
    def decorator(f):
        def wrapper(*args, **kwargs):
            newargs = dargs + args  # リストの結合
            newkwargs = {**kwargs, **dkwargs}  # 辞書の結合 (python3.5以上で動く)
            f(*newargs, **newkwargs)
        return wrapper
    return decorator


@args_joiner('darg', dkwarg=True)
def print_args(*args, **kwargs):
    print('args: {}, kwargs: {}'.format(args, kwargs))


# 以下と等価
'''
def print_args(*args, **kwargs):
    print('args: {}, kwargs: {}'.format(args, kwargs))
print_args = args_joiner('darg', dkwarg=True)(print_args)
'''


def main():
    print_args('arg', kwarg=False)


if __name__ == "__main__":
   main()
