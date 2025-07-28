#Write a program to check if a given key already exists in a dictionary.
sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
target_key = 2
if target_key in sample_dict:
    print(f"The targeted key {target_key} is present in the dictionary.")
else:
    print(f"The targeted key {target_key} is not present in the dictionary.")
