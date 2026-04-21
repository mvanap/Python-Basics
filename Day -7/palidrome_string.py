def palindrome_string(data):
    n = len(data) - 1
    new_string = ""
    if n == 0:
        return False
    while n >= 0:
        new_string = new_string + data[n]
        n -= 1
    return new_string == data

data = input("Enter the characters you want to check: ")
palindrome = palindrome_string(data)
print(f"The given data {data} is palindrome {palindrome}")