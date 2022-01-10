#You are required to write a program to sort the (name, age, height) tuples
#by ascending order where name is string, age and height are numbers. The
#tuples are input by console. The sort criteria is:
#1: Sort based on name;
#2: Then sort based on age;
#3: Then sort by score.
#The priority is that name > age > score.
lines = []
print("Enter the data:")
while True:
    data = input()
    if data:
        lines.append(data)
    else:
        break


tupData = tuple(lines)
sortedTuple = sorted(tupData,key = lambda i: (i[0],i[1],i[2]))

print(tupData)
print(sortedTuple)


#Tom,19,80
#John,20,90
#Jony,17,91
#Jony,17,93
#Json,21,85

