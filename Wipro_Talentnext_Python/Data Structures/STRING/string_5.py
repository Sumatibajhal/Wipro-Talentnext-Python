#Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive. For example if the inputs are "Wipro" and 3, then the output should be "propropro".
def n_copies(S, n):
    if n <= len(S):
        return S[-n:]*n

print(n_copies("Wipro", 3))