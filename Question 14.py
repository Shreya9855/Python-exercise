#Write a program that computes the net amount of a bank account based a transaction log from console input.
n = int(input("How many transaction do you have ? "))
print("Enter your transaction(W/D) : ")
transList = []
for i in range(n):
    trans = input()
    transList.append(trans)
W_list=[]
D_list = []
for i in transList:
    if i[0] == "W":
        W_list.append(i[2:])
    if i[0] == "D":
        D_list.append(i[2:])
totalD = sum([int(s) for s in D_list])
totalW = sum([int(s) for s in W_list])

print("Your total is : "  + str(totalD-totalW))
