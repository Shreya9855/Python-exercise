#Write a program that accepts a sentence and calculate the number of letters and digits.

string = input("Enter the string: ")
count_digits = 0
count_letters = 0
count_rem = 0
for i in string:
    if i.isalnum():
        if i.isalpha():
            count_letters +=1
        if i.isdigit():
            count_digits +=1
    else:
        count_rem +=1
        print(i)
print("You have entered " + string)
print("LETTERS: "+ str(count_letters))
print("DIGITS: "+ str(count_digits))
print("REMAINING: "+ str(count_rem))
