# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
passin = input("Enter the passwords: ")
passList = passin.split(",")
special = ["$","#","@"]
for char in passList:
    if len(char) >= 6 and len(char) <= 12:
        if any(c.isalnum for c in char):
            if any(c.upper for c in char):
                if any(c in special for c in char):
                    print("The valid password is " + char)



        





    


#ABd1234@1,a F1#,2w3E*,2We3345,aaaaa
