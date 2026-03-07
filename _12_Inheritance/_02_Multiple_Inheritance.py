# Parent Class 1
class Father:
    
    def skill_father(self):
        print("Father: Gardening")


# Parent Class 2
class Mother:
    
    def skill_mother(self):
        print("Mother: Cooking")


# Child Class inheriting from both parents
class Child(Father, Mother):

    def skill_child(self):
        print("Child: Programming")


# Create object
c = Child()

# Access methods from both parents
c.skill_father()
c.skill_mother()
c.skill_child()