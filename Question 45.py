#The Fibonacci Sequence is computed based on the following formula:
#f(n)=0 if n=0
#f(n)=1 if n=1
#f(n)=f(n-1)+f(n-2) if n>1
#Please write a program to compute the value of f(n) with a given n input by console.

n = int(input("Enter a number: "))
def fibo(n):
    if n == 0:
        result = 0
    if n == 1:
        result = 1
    elif n>1:
        result = fibo(n-1) + fibo(n-2)
    return result
print(fibo(n))

