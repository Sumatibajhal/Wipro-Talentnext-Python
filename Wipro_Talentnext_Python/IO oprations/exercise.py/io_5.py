#Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

filename = input("Enter file name: ")

try:
    with open(filename, 'r') as file:
        words = file.read().split()
        longest = max(words, key=len)
    print("Longest word in file:", longest)
except FileNotFoundError:
    print("Error: File not found.")
