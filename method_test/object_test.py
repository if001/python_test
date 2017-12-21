"""
オブジェクトのテスト

https://docs.python.jp/3/tutorial/classes.html
"""


class InstanceTest():
    def __init__(self):
        pass

    def instance_method(self, word):
        print("instance methods " + word)

    @staticmethod
    def instance_method2():
        print("unbound?")


def object_test(method):
    method("method in object")


def object_test2(method, word):
    method(word)


def main():
    # まずは普通に
    instance_test = InstanceTest()
    instance_test.instance_method("instance !!")

    # オブジェクトを確認
    print(instance_test.instance_method("instance !!"))
    print(instance_test.instance_method)
    print(InstanceTest.instance_method2)

    # オブジェクトを受け取ってみる
    method = instance_test.instance_method

    # これは表示されない
    print("me",method("method ??"))


    # これはいける
    object_test(method)

    # こんなのもできる
    object_test2(method, "args")


if __name__ == "__main__":
   main()
