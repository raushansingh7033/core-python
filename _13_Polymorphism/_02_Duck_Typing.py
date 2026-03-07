class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

def make_fly(obj):
    obj.fly()

b = Bird()
a = Airplane()

make_fly(b)
make_fly(a)