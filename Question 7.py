#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

words = input("Enter your strings : ")
word_list = words.split(",")
print(sorted(word_list))