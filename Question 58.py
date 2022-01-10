#Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person:
    def __init__(self):
        pass
    def setGender(self,gender):
        self.gender = gender
    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self):
        super().__init__()
        self.gender = "Male"
    def getGender(self):
        return self.gender

class Female(Person):
    def __init__(self):
        super().__init__()
        self.gender = "Female"
    def getGender(self):
        return self.gender

m = Male()
print(m.getGender())
f = Female()
print(f.getGender())
p = Person()
p.setGender("Male")
print(p.getGender())