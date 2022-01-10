#Define a function which can compute the sum of two numbers.

def Sum(n1,n2):
    return n1 + n2

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2 : "))
sum = Sum(n1,n2)
print("The sum is : " + str(sum))