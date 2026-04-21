def max_list(numbers):
    max_number = numbers[0]

    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number


numbers = list(map(int, input("Enter the list you want: ").split()))
max_number = max_list(numbers)
print(f"The max number in the list {numbers} is {max_number}.")

