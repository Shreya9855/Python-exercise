#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.


words= input("Enter the string: ")
no_whitespace = " ".join(words.split())
list = no_whitespace.split(' ')
list.sort()
ulist = [] 
[ulist.append(x) for x in list if x not in ulist]
string = ""
for i in ulist:
    string = string + i + " "
print(string)