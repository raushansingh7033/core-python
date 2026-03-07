class Employee:

    def __init__(self):

        # public
        self.name = "Alice"

        # protected
        self._salary = 50000

        # private
        self.__bonus = 10000


emp = Employee()

print(emp.name)              # public
print(emp._salary)           # protected
print(emp._Employee__bonus)  # private via name mangling