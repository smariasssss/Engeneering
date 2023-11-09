class Russian:
    @staticmethod
    def greeting():
        print("Привет")


class English:
    @staticmethod
    def greeting():
        print("Hello")


def greet(Language):
    Language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
