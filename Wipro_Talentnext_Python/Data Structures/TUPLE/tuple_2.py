#Write a program to check whether an element exists in a tuple or not.

tuple_2 = (10, 20, 30, 40, 50)
element = 30
if element in tuple_2:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")