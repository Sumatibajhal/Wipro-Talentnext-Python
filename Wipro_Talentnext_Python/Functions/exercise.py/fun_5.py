#Write a function to print the even numbers from a given list. List is passed to the function as an argument.

def even_list(inp_list):
    even = []
    for i in inp_list:
        if i % 2 == 0:
            even.append(i)
        else:
            continue
    print(even)

Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list(Sample_List)
