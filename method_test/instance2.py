"""
http://d.hatena.ne.jp/kiwamu_i/20130401/1364821445

インスタンスメソッド・クラスメソッド・スタティックメソッド
のテスト
"""


class InstanceTest():
    def __init__(self):
        self.value = 0
        self.__private_value = 0


    def instance_method(self):
        print("instance method!!")


    def instance_method2():
        """
        引数を与えないと、staticmethodのように振る舞える
        ただしこれはPEP8的には怒られる
        python2ではエラー
        """
        print("instance method2")


    def __private_method(self):
        self.value = 2
        print("private")


def main():
    instance_test = InstanceTest()
    # instance_test.instance_method2()

    InstanceTest.instance_method2()

    # private 変数へのアクセスはできない
    print(instance_test.__private_value)

    # private methodへのアクセスはできない
    print(instance_test.value)
    instance_test.__private_method()
    print(instance_test.value)

if __name__ == "__main__":
    main()
