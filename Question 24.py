#Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

def max_len(str1,str2):
    if len(str1) == len(str2):
        return str1 + "\n" + str2
    else:
        if len(str1) > len(str2):
            return str1
        else:
            return str2

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(max_len(str1,str2))