#Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".
def remove_x(S):
    if len(S) >= 0 and S[0] == 'x':
        S = S[1:]
    if len(S) >= 0 and S[-1] == 'x':
        S = S[:-1]
    return S

print(remove_x('xHellox'))
    
