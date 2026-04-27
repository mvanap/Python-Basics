file_path = r"D:\MyFiles\Projects\Python-Basics\Day -10\data.txt"

with open(file_path, "r") as f:
    line_count = 0
    word_count = 0
    repeat_count = 0
    for line in f:
        line_count += 1
        words = line.lower().split()
        for word in words:
            word_count += 1
            if word == "python":
                repeat_count += 1

with open(r"D:\MyFiles\Projects\Python-Basics\Day -10\output.txt", "w") as f:
    f.write(f"The number of lines is {line_count}.\nThe numer of words are {word_count}.\nThe repeat count of python is {repeat_count}")

