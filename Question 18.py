#Define a class, which have a class parameter and have a same instance parameter.
class Game:
    name = "Football"
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name

g = Game("Hockey")
print(Game.name)
print(g.name)
print(g.getName())