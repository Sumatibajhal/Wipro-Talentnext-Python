#Write a program to check if a given number is Positive, Negative or Zero.
def intchecks(a):
    if a > 0:
        print(f'The number {a} is positive.')
    elif a < 0:
        print(f'The number {a} is negative.')
    else:
        print(f'The number {a} is Zero.')

num = float(input("Enter the number: "))
intchecks(num)



