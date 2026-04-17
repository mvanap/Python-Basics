print("Return the Sum of N")

def sum_number(value):
    total = 0
    for i in range(1,value+1):
        total += i
    return total

value = int(input("Enter the number: "))
result = sum_number(value)
print(f"The sum of the {value} is {result}")
