# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

n = int(input("Enter a number: "))
if(n > 0):
    sum = 0
    for i in range(n+1):
            sum  += i/(i+1)
    print(round(sum,2))
