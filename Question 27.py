#Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

def Squaredict(number):
    dict = {}
    for i in range(1,number+1):
        dict[i] = pow(i,2)
    return dict

n = int(input("Enter a number till the square needed: "))
print(Squaredict(n))
        