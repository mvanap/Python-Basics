def factorial(number):
    target = 1
    for i in range(1, number + 1):
        target = target * i
    return target
number = int(input("Enter the number: "))
factorial_of = factorial(number)
print(f"The factorial of {number} is {factorial_of}")