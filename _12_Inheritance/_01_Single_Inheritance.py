# Parent Class
class Person:

    # Parent constructor
    def __init__(self, name, age):
        print("Parent Constructor Called")
        self.name = name
        self.age = age

    # Parent method
    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class
class Student(Person):  # Single Inheritance

    # Child constructor
    def __init__(self, name, age, course):

        # Calling parent constructor using super()
        super().__init__(name, age)

        print("Child Constructor Called")

        self.course = course

    # Child method
    def show_student(self):
        print("Course:", self.course)


# Create object
s1 = Student("Alice", 21, "Computer Science")

# Access parent method
s1.show_person()

# Access child method
s1.show_student()