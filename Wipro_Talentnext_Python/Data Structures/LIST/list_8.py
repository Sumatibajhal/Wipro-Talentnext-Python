#Write a program to remove the first occurrence of a specified element from a list.
my_list = [1, 2, 3, 2, 4, 5]
element = int(input("Enter the element to remove: "))

try:
    my_list.remove(element)
    print(my_list)
except ValueError:
    print(f"{element} not found in the list.")