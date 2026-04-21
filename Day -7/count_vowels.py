def count_vowels(received):
    vowel={'a','e','i','o','u'}
    count = 0
    received = received.lower()
    for character in received:
        if character in vowel:
            count += 1
    return count

received = input("Enter the string you want to check whether it has vowels or not: ")
result = count_vowels(received)
print(f"The number of vowels for the given characters {received} is {result}.")

