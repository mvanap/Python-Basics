def check_even(value):
    if value % 2 == 0:
        return True
    else:
        return False
value = int(input("Enter the Number: "))
result = check_even(value)
print(f"The Number is Even? {result}")