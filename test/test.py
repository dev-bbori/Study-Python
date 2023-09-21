class Animal:
    def __init__(self, age):
        self.age = age

    def eat(self):
        pass


Animal().__reduce__()
