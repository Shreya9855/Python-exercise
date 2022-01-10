#Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).


def squareTuple():
    list = []
    for i in range(1,20+1):
        list.append(pow(i,2))
    return tuple(list)

tup = squareTuple()
print(tup)
print(type(tup))
