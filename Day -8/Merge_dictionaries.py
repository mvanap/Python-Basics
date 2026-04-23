def take_input(range_set):
    data = {}
    for _ in range(range_set):
        key = input("Enter the key for the set: ")
        key_id = int(input("Enter the value for the set: "))
        data[key] = key_id
    print("The Data for set has been inserted")
    return data
    

def merge_dictionary(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1
    

n = int(input("Enter the range for set 1: "))
m = int(input("Enter the range for set 2: "))
dict1 = {}
dict2 = {}

dict1 = take_input(n)
dict2 = take_input(m)

merged_dictionary = merge_dictionary(dict1, dict2)
print(merged_dictionary)
