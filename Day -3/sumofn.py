print("Sum of n numbers")

number = int(input("Enter the value of n: "))
total = 0
for i in range(1, number + 1):
    total += i
print(f"The sum of the numbers from 0 to {number} is {total}")