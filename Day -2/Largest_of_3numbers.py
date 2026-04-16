print("Check which is the largest number among the Three given numbers.")

num1 = int(input("Please enter the First number: "))
num2 = int(input("Please enter the Second number: "))
num3 = int(input("Please enter the Third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number in the given vales are {largest}.")