class Factory:
    def __init__(self,material,zips):
        self.material=material
        self.zips=zips
class Bhopal(Factory):
    def __init__(self,material,zips,color):
        super().__init__(material,zips)
        self.color=color
class Pune(Bhopal):
    def __init__(self,material,zips,color,pockets):
        super().__init__(material,zips,color)
        self.pockets=pockets
    def show(self):
        print(f"{self.material},{self.zips},{self.color},{self.pockets}")

obj=Pune("polyester",5,"blue",6)
obj.show()