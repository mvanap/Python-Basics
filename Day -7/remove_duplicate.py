def remove_duplicate(data):
    seen = ""
    for char in data:
        if char not in seen:
            seen = seen + char
    return seen

data = input("Enter the string you want to check: ")
result = remove_duplicate(data)
print(f"The result of the given data {data} is {result}.")