class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


p = Person(20)

print(p.get_age())

p.set_age(25)

print(p.get_age())