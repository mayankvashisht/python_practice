# python is pure object oriented languge.
# objects has properties and functions and occupie some space in memory.
# objects - 
#   functions
#   properties

# classes is a blue print for object to define the properties and functions in object.

# class Tiger:
#     legs = 4
#     color = 'brown'

# a = int(12)
# # Tiger.color = "blue"
# print(Tiger.color)

# sheru = Tiger()
# peru = Tiger()
# print(sheru.legs)
# sheru.legs = 5
# print(sheru.legs)
# print(peru.color, peru.legs)



# class Animal:
#     # numberOfLegs = 0
#     # color = 0
#     def __init__(self, a, b) -> None:
#         self.numberOfLegs = a
#         self.color = b
#         print("object created", a, b)


# obj1 = Animal(6, "black")
# # obj1.numberOfLegs
# print(obj1.numberOfLegs, obj1.color)
# # b = Animal()




class Array:

    def __init__(self, size):
        self.mylist = []
        self.size = size


    def addItemInList(self, a):
        self.mylist.append(a)

    def getAtIndex(self, ind):
        return self.mylist[ind]

    def showItems(self):
        print("item in list are: ")
        for item in self.mylist:
            print(item)

    def showSize(self):
        print('print size of array is: ', self.size)


myArr = Array()
myArr2 = Array(90)
# myArr.addItemInList("mukul")
# myArr.addItemInList("mayank")
# myArr.addItemInList(123123)
# myArr.addItemInList("skdfskdjfh")

# print(myArr.getAtIndex(2))

myArr.showItems()

