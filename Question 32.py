#Write a program which can filter even numbers in a list by using filter function.

lst = [1,2,3,4,5,6,7,8,9]
evenOnly = list(filter(lambda n: n % 2 ==0 ,lst))
print(evenOnly)