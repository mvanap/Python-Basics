class Employee:
    def __init__(self,name,salary):
        self.name  = name
        self.salary = salary

    def increase_salary(self,amount):
        self.salary = self.salary + amount
        return self.salary 

emp1 = Employee("Manideep", 21000)
emp2 = Employee("Swati", 70000)

emp1_result = emp1.increase_salary(500)
print(emp1_result)
