#Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

def dict_square():
    dict = {}
    for i in range(1,3+1):
        dict[i] = i**2
    return dict
        
print(dict_square())