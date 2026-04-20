def reverse_value(value):
    reversed_value = 0

    while value > 0:
        remainder = value % 10
        #The remainder should be multiplied by 10 for the new remainder to be added.
        reversed_value = reversed_value * 10 + remainder
        #By removing the remainder we can use cofiecient to assign value.
        value = value // 10

    return reversed_value
    
value = int(input("ENter the value you want to reverse: "))
reversed = reverse_value(value)

print(f"The give number {value} is reversed as {reversed}")