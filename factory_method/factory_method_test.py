from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):

    @abstractmethod
    def use(self):
        pass


class Factory(metaclass=ABCMeta):

    @abstractmethod
    def _create_product(self, owner):
        pass

    @abstractmethod
    def _register_product(self, product):
        pass

    def create(self, owner):
        self.__p = self._create_product(owner)
        self._register_product(self.__p)
        return self.__p


class IDCard(Product):

    def __init__(self, owner):
        self.__owner = owner
        print(self.__owner + 'のカードを作成します')

    def use(self):
        print(self.__owner + 'のカードを使います')

    def get_owner(self):
        return self.__owner



class IDCardFactory(Factory):

    def __init__(self):
        self.__registed = []

    def _create_product(self, owner):
        return IDCard(owner)

    def _register_product(self, product):
        self.__registed.append(product.get_owner())


def main():
    factory = IDCardFactory()
    card1 = factory.create('結城浩')

    card1.use()


if __name__ == '__main__':
    main()
