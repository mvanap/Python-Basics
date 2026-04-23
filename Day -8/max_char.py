def max_char(word):
    freq = {}

    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    max_char = ''
    max_count = 0
    for char in freq:
        if freq[char] > max_count:
            max_count = freq[char]
            max_char = char
    return max_char

word = input("Enter the word you want to insert: ")
result = max_char(word)
print(result)