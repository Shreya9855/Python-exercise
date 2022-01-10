#Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def Square(n):
    list = []
    for i in range(1,n+1):
        list.append(i*i)
    return list

n = int(input("Enter number of items in the list: "))
print(Square(n))