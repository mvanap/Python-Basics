def count_words(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


sentence = input("Enter the sentence you want to insert: ")
sentence = sentence.lower()
words = sentence.split()
result = count_words(words)
print(result)
