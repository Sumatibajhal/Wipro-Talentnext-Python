#Write a program to print the number of occurrences of a specified element in a list.
list_str = input("Enter elements of the list separated by spaces: ")
my_list = list(map(int, list_str.split()))

element = int(input("Enter the element to count: "))

count = my_list.count(element)

print(f"The element {element} occurs {count} time(s) in the list.")