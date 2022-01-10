#Define a function that can accept two strings as input and concatenate them and then print it in console

def concate(str1,str2):
    return str1 + str2
str1 = input("Enter a string: ")
str2 = input("Enter another string: ")
print("{} + {} = {}".format(str1,str2,concate(str1,str2)))