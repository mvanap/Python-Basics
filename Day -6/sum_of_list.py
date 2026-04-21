def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

numbers = list(map(int, input("Enter the numbers: ").split()))
sum_list = sum_of_list(numbers)
print(f"The sum of the {numbers} is {sum_list}.")