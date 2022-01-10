#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

linenumber = int(input("How many lines do you wanna enter : "))
line = []
print("Enter the strings")
for i in range(linenumber):
    line.append(input())
string = " "
for l in line:
    string += l + " "
print(string.upper())
