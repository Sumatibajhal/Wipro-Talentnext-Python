#Write a program to reverse a given number and print.
num = int(input("Enter a number: "))
rev = 0

while num != 0:
    digit = num % 10         
    rev = rev * 10 + digit  
    num //= 10               

print("Reversed number:", rev)
