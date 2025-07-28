#Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("Keys:")
for key in sample_dict:
    print(key)

print("Values:")
for value in sample_dict.values():
    print(value)

print("Keys and Values:")
for key, value in sample_dict.items():
    print(f"{key} : {value}")
