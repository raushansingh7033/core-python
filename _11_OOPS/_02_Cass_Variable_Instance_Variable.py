class Student:

    school = "ABC School"   # Class variable

    def __init__(self, name, age):
        self.name = name    # Instance variable
        self.age = age      # Instance variable

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", Student.school)
        print()

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
s1.display()
s2.display()
        