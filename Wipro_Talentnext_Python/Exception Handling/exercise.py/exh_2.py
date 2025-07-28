#Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print("The number is prime.")
    else:
        print("The number is not prime.")
except ValueError:
    print("Error: Please enter a valid integer.")
