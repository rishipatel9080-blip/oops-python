class Animal: #parent class
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"your name is {self.name}")
class Human(Animal): #child class
    def __init__(self,name,age):
        super().__init__(name) #calls parent class's __init__ method
        self.age=age
    def show(self):
        print(f"your name is {self.name} and your age is {self.age}")
animal=Animal("lion")
animal.show()
person=Human("rishi",19)
person.show()
