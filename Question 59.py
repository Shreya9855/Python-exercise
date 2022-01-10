# Please write a program which accepts a string from console and print it in reverse order.

string = input("Enter a string: ")
strList = string.split(" ")
for i in strList[::-1]:
    print(i[::-1],end=" ")