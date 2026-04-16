print("Counting the no of even numbers present in a given number.")
event_count = 0
number = int(input("Enter the number you want to: "))
for i in range(1,number+1):
    if i % 2 == 0:
        event_count += 1
print(f"The number of even numbers in {number} is {event_count}.")
     