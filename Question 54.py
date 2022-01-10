#Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
subject = ["I","You"]
verb = ["Play","Love"]
object = ["Hockey","Football"]
subjectList = []
#random.choice(subject) + " " + random.choice(verb) + " " + random.choice(object)
for i in range(2):
    for j in range(2):
        for k in range(2):
            sentence = subject[i]+ " " + verb[j]+ " " + object[k]
            subjectList.append(sentence)
print(subjectList)

