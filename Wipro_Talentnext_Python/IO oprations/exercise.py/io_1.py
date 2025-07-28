#Write a program to read the entire content from a txt file and display it to the user.

filename = input("Enter the file name: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile Contents:\n", content)
except FileNotFoundError:
    print("Error: File not found.")
