class Animal:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"your name is {self.name}")
class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def show(self):
        print(f"your name is {self.name} and your age is {self.age}")
animal=Animal("lion")
animal.show()
person=Human("rishi",19)
person.show()