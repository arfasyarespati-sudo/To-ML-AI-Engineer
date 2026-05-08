class Dog:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def bark(self):
        print("woof woof")

    def walk(self):
        print("thump thump")
    
    def jump(self):
        print("hop hop")

d = Dog("Rusell", 15, 75)
print(d.getName())
d.setName("Wally")
print(d.getName())

