#Write a program to check if a given number is odd or even.
def evenodd(n):
    if n % 2 == 0:
        print(f"The number {n} is even.")
    else:
        print(f"The number {n} is odd.")

num = float(input("Enter the number: "))
evenodd(num)