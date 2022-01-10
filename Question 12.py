#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

string = input("Enter a string : ")
count_upper = 0
count_lower = 0
for letter in string:
    if letter.isalpha():
        if letter.isupper():
            count_upper+=1
        if letter.islower():
            count_lower+=1

print("You have entered: " + string)
print("UPPER : " + str(count_upper))
print("LOWER : " +str(count_lower))