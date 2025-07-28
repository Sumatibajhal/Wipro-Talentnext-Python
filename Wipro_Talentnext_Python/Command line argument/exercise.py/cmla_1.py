#Write a program to accept two numbers as command line arguments and display their sum.
import sys
if len(sys.argv) != 3:
    print("Usage: python script.py 5 6")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
      
        print("Sum:", num1 + num2)
    except ValueError:
        print("Please enter valid numbers.")
