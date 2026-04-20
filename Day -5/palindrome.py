def palindrome(value):
    original_value = value
    reversed_value = 0
    if value == 0:
        return True
    while value > 0:
        remainder = value % 10
        reversed_value = reversed_value * 10 + remainder
        value = value // 10
    return reversed_value == original_value

value = int(input("Enter the value to check palindrome: "))
checked = palindrome(value)
print(f"The given value {value} is {checked}.")