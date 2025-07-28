#Write a program to read contents from a txt file line by line and store each line into a list.

filename = input("Enter file name: ")

try:
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    print("Lines stored in list:", lines)
except FileNotFoundError:
    print("Error: File not found.")
