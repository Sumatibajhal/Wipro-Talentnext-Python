#Write a program to replace last value of tuples in a list to 100.
Original_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

new_list = []
for tpl in Original_list:
    temp_list = list(tpl)
    temp_list[-1] = 100
    new_list.append(tuple(temp_list))

print(new_list)
