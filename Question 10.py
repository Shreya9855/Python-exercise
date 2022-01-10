#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence

number = input("Enter a 4 digit binary number :")
list = number.split(",")
res = ""
    
for i in list:
    if len(i) == 4:
        if int(i,2) % 5 == 0:
            res+= i + " "
    else:
        print("The number should be 4 digit number")
print(res)
