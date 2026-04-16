print("We are here to identify the age catefory based on the iformation: 18 < minors, 18 > adults, 60 > senior citizens.")

age = int(input("Please enter your age: "))

if age < 18:
    print(f"You are a minor and your age is {age}.")
elif age < 60:
    print(f"You are an adult and your age is {age}.")
else:
    print(f"You are a Senior Citizen and your age is {age}.")