
"""
decorator test
https://qiita.com/makky05/items/1be6cf0f1f238b5ba01b
"""


def args_logger(f):
    def wrapper(*args, **kwargs):

        print("----start-----")
        f(*args, **kwargs)
        print("----end-----")
        # print('args: {}, kwargs: {}'.format(args, kwargs))
    return wrapper

@args_logger
def print_message(msg):
    print(msg)


def main():
    print_message('hello')


if __name__ == "__main__":
   main()
