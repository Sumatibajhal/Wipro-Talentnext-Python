#Write a program to sum all the values in a dictionary, considering the values will be of int type.
def total_values(Dictionary):
    total_sum = 0
    for value in Dictionary.values():
        total_sum += value
    return total_sum

dict_6 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(total_values(dict_6))