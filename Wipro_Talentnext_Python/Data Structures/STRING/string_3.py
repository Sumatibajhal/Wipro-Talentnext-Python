#Given a string, return a new string made of n copies of the first 2 chars of the original stringwhere n is the length of the string. The string length will be >=2.If input is "Wipro" then output should be "WiWiWiWiwi".
def n_copies(S):
    n = len(S)
    return S[0:2]*n

print(n_copies("Wipro"))