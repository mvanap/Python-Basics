while True:
    try:
        user_value = int(input("Enter the number: "))
        print(f"Entered value {user_value} is valid.")
        break
    except ValueError:
        print("Enter valid number.")