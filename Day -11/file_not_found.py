dir = "D:/MyFiles/Projects/Python-Basics/Day -11/"

while True:
    file_name = input("Enter the name of the file: ")
    file_path = f"{dir}{file_name}"
    if not file_name:
        print("Eter the file name again, epmty file name cant be accepted.")
        continue

    try:
        with open(file_path, "r") as f:
            print(f.read())
        break

    except FileNotFoundError:
        print(f"The file {file_path} is not found, try again.")