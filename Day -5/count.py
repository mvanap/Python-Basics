def count_n(value):
    if value == 0:
        return 1
    count = 0 
    while value > 0:
        value = value // 10
        count += 1
    return count

value = int(input("Please enter the value you want to check: "))
count = count_n(value)
print(f"The count of the value {value} is {count}. ")