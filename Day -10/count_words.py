file_path = r"D:\MyFiles\Projects\Python-Basics\Day -10\data.txt"
with open(file_path, "r") as f:
    total_words = 0
    for line in f:
        words = line.split()
        print(words)
        total_words += len(words)

print(f"The total number of the words are {total_words}.")
    
