# Grandparent class
class Grandparent:

    def grandparent_method(self):
        print("This is Grandparent method")


# Parent class inherits from Grandparent
class Parent(Grandparent):

    def parent_method(self):
        print("This is Parent method")


# Child class inherits from Parent
class Child(Parent):

    def child_method(self):
        print("This is Child method")


# Create object of Child
c = Child()

# Access methods from all levels
c.grandparent_method()   # from Grandparent
c.parent_method()        # from Parent
c.child_method()         # from Child