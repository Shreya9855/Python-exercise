#Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

import re
words = input("Enter the words: ")
word_list = words.split(" ")
digit = []
for word in word_list:
    if word.isdigit():
        digit.append(word)

#Using regex
print(digit)
find = re.findall('\d+',words)
print(find)