#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

num = input("Enter the set of numbers")
list = num.split(",")
print(list)
tup = tuple(list)
print(tup)