class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def increase_salary(self,amount):
        if self.salary < 0:
            print("The amount value provided shouldnt be negative.")
        else:
            self.salary = self.salary + amount
    
    def apply_bonus(self,percent):
        bonus = self.salary * ( percent / 100)
        self.salary = self.salary + bonus
        print(f"The Salary with bonus percentage {percent} is {self.salary}")

    def display(self):
        print(f"Name: {self.name}, Salary : {self.salary}")

emp1 = Employee("Manideep Shankar", 70000)

emp1.apply_bonus(10)
emp1.display()