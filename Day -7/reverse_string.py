def reverse_string(data):
    final_index = len(data) - 1
    result = ""
    while final_index >= 0:
        result = result + data[final_index]
        final_index -= 1
    return result

reversed = reverse_string("Mani")
print(reversed)