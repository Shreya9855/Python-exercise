#With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

list1 = [12,24,35,24,88,120,155,88,120,155]
setA = set(list1)
new_list = list(setA)
new_list.sort()
print(new_list)