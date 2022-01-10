#. Define a function that can convert a integer into a string and print it in console.

def intToString(number):
    return str(number)

n = int(input("Enter a number : "))
print("The number you entered is {} of type {} and now it is of type {}".format(n,type(n),type(intToString(n))))