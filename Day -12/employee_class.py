class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name : {self.name}, Salary: {self.salary}"

emp1 = Employee("Manideep", 21000)
emp2 = Employee("Swati", 20000)

print(emp1)
print(emp2)