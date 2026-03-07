class Student:

    # Constructor with default values
    # Works as Default Constructor + Parameterized Constructor
    def __init__(self, name="Unknown", age=0):
        print("Constructor Executed")   # runs automatically
        
        # instance variables
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# -------------------------------
#  Default Constructor Example
# -------------------------------

print("Default Constructor Example")

s1 = Student()      # no arguments passed
s1.display()

# Output:
# Name: Unknown
# Age: 0


# --------------------------------
#  Parameterized Constructor
# --------------------------------

print("\nParameterized Constructor Example")

s2 = Student("Alice", 22)   # passing values
s2.display()

# Output:
# Name: Alice
# Age: 22


# --------------------------------
# Constructor Overloading Concept
# --------------------------------
# Python does NOT support real constructor overloading
# Instead we use default arguments or *args

print("\nConstructor Overloading Concept")

s3 = Student("Bob")     # only name provided
s3.display()

