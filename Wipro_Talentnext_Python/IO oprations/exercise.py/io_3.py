#Write a program to accept input from user and append it to a txt file.

filename = input("Enter file name: ")
user_input = input("Enter text to append: ")

try:
    with open(filename, 'a') as file:
        file.write(user_input + '\n')
    print("Text appended successfully.")
except Exception as e:
    print("An error occurred:", e)
