#Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py Hello and welcome!")
else:
    filename = sys.argv[0]
    msg = " ".join(sys.argv[1:])
    print(f"File Name: {filename}")
    print(f"Welcome Message: {msg}")
