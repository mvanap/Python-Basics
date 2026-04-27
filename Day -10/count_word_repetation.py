file_path = r"D:\MyFiles\Projects\Python-Basics\Day -10\data.txt"

with open(file_path, "r") as f:
    count = 0
    for line in f:
        line = line.lower()
        words = line.split()
        for word in words:
            if word == "python":
                count += 1 

print(f"The Python word repeated in the file of {count} times.")
