#Write a program to insert a new item before the second element in an existing list.
list_6 = [45,78,65,94,12]

item = int(input("Enter an item to be inserted: "))
list_6.insert(1,item)
print(list_6)