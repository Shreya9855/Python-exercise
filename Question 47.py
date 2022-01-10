#Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console

n = int(input("Enter a number: "))
def num_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield(i)

for i in num_generator(n+1):
    print(i,end = ",")