#. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

def Square(n):
    list = []
    for i in range(1,n+1):
        list.append(i*i)
    return list[5:]

n = int(input("Enter number of items in the list: "))
print("Without the first five elements: ")
print(Square(n))