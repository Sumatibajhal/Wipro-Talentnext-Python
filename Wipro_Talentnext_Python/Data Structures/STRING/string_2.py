#Write a program that will check whether a given String is Palindrome or not.
def is_palindrome(S):
    S = S.replace(" ","").lower()
    return S == S[::-1]

print(is_palindrome("Madam"))
print(is_palindrome("Hello"))


