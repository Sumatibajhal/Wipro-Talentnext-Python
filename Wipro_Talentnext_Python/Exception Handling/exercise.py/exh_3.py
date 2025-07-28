#Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
try:
    filename = input("Enter the file name: ")
    with open(filename, 'r') as file:
        content = file.read()
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
