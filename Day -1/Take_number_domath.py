print("Insert the two numbers you want to do calculations with.")

num1 = int(input("Please enter the number 1: "))
num2 = int(input("Please enter the number 2: "))

total = num1 + num2
subtraction = num1 - num2
multiply = num1*num2

if num2 == 0:
    divided = "Undefined (cannot divide by zero)"
else:
    divided = num1/num2


print(f"The Sum of the two numbers is {total}.")
print(f"The Difference between the two numbers is {subtraction}.")
print(f"The Multiplication of the two numbers is {multiply}.")
print(f"The Division of the two numbers is {divided}.")