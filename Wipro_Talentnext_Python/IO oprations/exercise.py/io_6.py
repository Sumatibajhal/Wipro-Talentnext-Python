#Write a program to count the frequency of a user entered word in a txt file.

filename = input("Enter file name: ")
search_word = input("Enter word to search: ")

try:
    with open(filename, 'r') as file:
        content = file.read().lower()
        count = content.split().count(search_word.lower())
    print(f"Frequency of '{search_word}' in file:", count)
except FileNotFoundError:
    print("Error: File not found")
