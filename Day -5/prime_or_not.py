print("Validate Prime or not")
def prime_or_not(value):
    if value <= 1:
        return False
    
    for i in range(2, value):
        if value % i == 0:
            return False
    return True

value = int(input("Enter the number ou want to check: "))
result = prime_or_not(value)
print(f"The given value {value} is prime? {result}")
                
    