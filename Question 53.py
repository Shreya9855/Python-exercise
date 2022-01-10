#Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

import random
list=[]
for i in range(100+1):
    if(i%5 == 0 and i%7==0):
        list.append(i)
print(list)
r = random.choice(list)
print(r)