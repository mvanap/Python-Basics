def count_frequency(data):
    freq = {}
    for char in data:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
                    

data = input("Enter the Characters: ")
result = count_frequency(data)
print(f"The result is {result}")