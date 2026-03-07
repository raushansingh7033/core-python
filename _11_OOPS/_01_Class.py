class Student:
  def __init__(self,name,age,roll_no):
    self.name=name
    self.age=age
    self.roll_no=roll_no
  def display(self):
    print("Name:",self.name)
    print("Age:",self.age)
    print("Roll No:",self.roll_no)

s1=Student("Alice",20,101)
s1.display()    