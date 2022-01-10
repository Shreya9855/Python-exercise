#Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1 with a given n input by console (n>0).

n = int(input("Enter a number: "))
def recursion(n):   
    if n == 0 :
        result = 1
    else:
        result = recursion(n-1) + 100
    return result


print(recursion(n))
