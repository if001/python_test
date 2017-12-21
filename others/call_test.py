"""
__call__は関数っぽく呼び出したら発動
"""


class A:
    def __init__(self, a):
        self.a = a
        print("A init")

    def __call__(self, b):
        print("A call")
        print(b + self.a)


def main():
    a = A(1)
    a(2)
    a(3)
    
if __name__ == "__main__":
    main()
