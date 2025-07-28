#Write a program to find the index of an item in a tuple.
tuple_4 = (10, 20, 30, 40, 50, 20)
item = 20

try:
    index = tuple_4.index(item)
    print(f"The item {item} is found at index: {index}")
except ValueError:
    print(f"The item {item} is not found in the tuple.")