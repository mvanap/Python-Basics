def reverse_list(numbers):
    i = 0
    n = len(numbers) - 1
    while i < n:
        temp = numbers[i]
        numbers[i] = numbers[n]
        numbers[n] = temp
        i += 1
        n -= 1

    return numbers

numbers = list(map(int, input("Enter the list: ").split()))
reversed = reverse_list(numbers)
print(reversed)