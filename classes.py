class BaseClass:
    def __init__(self, name, stan):
        self.name = name
        self.standard = stan

    def printHello(self):
        print("hello")

class DerivedClass(BaseClass):
    def ShowName(self):
        print(self.name)


obj = DerivedClass("mukul", "fifth")
print(obj.standard, obj.name)
obj.printHello()
obj.ShowName()