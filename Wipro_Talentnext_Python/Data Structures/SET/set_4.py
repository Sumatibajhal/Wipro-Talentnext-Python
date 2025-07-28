# Write a program to find the maximum and minimum value in a set.
my_set = {10, 5, 20, 15, 8, 25}

if my_set:
    max_val = min_val = next(iter(my_set)) 

    for num in my_set:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    print(f"Maximum value: {max_val}")
    print(f"Minimum value: {min_val}")
else:
    print("The set is empty.")