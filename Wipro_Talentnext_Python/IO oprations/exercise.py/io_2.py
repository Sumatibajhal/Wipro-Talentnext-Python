#Write a program to read first n lines from a txt file. Get n as user input.

filename = input("Enter the file name: ")

try:
    n = int(input("Enter the number of lines to read: "))
    with open(filename, 'r') as file:
        for _ in range(n):
            print(file.readline(), end="")
except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: enter a valid integer.")
