#Write a function to return the sum of all numbers in a list.
def list_sum(List):
    sum = 0
    for i in List:
        sum += i
    return sum

Sample_List = [8, 2, 3, 0, 7]
print(list_sum(Sample_List))