class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def increase_salary(self,amount):
        self.salary = self.salary + amount
        return self.salary
    
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
    
emp1 = Employee("Manideep Shankar", 70000)
emp2 = Employee("Swati Garje", 70000)
emp1.display()
