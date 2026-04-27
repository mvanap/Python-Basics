file_path = r"D:\MyFiles\Projects\Python-Basics\Day -10\data.txt"
with open(file_path, "r") as f:
    count = 0
    for line in f:
        count += 1

print(f"The total number of lines present in the file is {count}.")