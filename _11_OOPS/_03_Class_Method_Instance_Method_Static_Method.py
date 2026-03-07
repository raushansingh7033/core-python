class Employee:

    # Class variable
    company = "TechCorp"
    total_employees = 0

    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    # Instance Method
    def show_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)

    # Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    #Static Method
    @staticmethod
    def is_high_salary(salary):
        if salary > 50000:
            return True
        return False
    

# Creating instances of Employee
emp1 = Employee("Alice", 60000)
emp2 = Employee("Bob", 45000)
# Displaying employee details
emp1.show_employee()
emp2.show_employee()

