"""
http://d.hatena.ne.jp/kiwamu_i/20130401/1364821445

インスタンスメソッド・クラスメソッド・スタティックメソッド
のテスト
"""


class InstanceTest():
    def instance_method(self):
        print("instance method!!")


    def instance_method2():
        """
        引数を与えないと、staticmethodのように振る舞える
        ただしこれはPEP8的には怒られる
        python2ではエラー
        """
        print("instance method2")


class StaticTest():
    class_value = 1

    def __init__(self):
        self.instance_value = 1

    @staticmethod
    def static_method():
        print("static method!!")

    @staticmethod
    def static_method2(self):
        print("static method2!!")


class OverRideStaticTest(StaticTest):
    """
    overrideしてみる
    staticmethodデコレーターなくてもいける
    """
    @staticmethod
    def over_static_method():
        print("over static!!")


    """
    overrideしてみる
    """
    def over_static_method2(self):
        print("over static 2 !!")


def main():
    instance_test = InstanceTest()
    instance_test.instance_method()

    # こっちはいける
    InstanceTest.instance_method2()
    # これはダメ
    # instance_test.instance_method2()


    # staticmethodを呼び出す
    StaticTest.static_method()

    # static methodだけどインスタンス化もできる
    static_test = StaticTest()
    static_test.static_method()


    # これは引数が足りないのでエラー
    # static_test.static_method()
    # 無理やりクラスを引数にとってみる
    static_test.static_method2(StaticTest)
    # 無理やりクラスを引数にとってみる(これでも通る)
    static_test.static_method2(StaticTest())


    # override
    OverRideStaticTest.over_static_method()
    # OverRideStaticTest.static_method2()

if __name__ == "__main__":
    main()
