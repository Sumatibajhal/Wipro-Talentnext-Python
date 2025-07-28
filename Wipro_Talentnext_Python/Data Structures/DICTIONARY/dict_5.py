#Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
dict_5 = {}

for i in range(1,16):
    square = i*i
    dict_5[i] = square
print(dict_5)