def count_even_list(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

numbers = list(map(int, input("Enter the list: ").split()))
count_value = count_even_list(numbers)

print(f"The given list is {numbers} and the count of even numbers is {count_value}")