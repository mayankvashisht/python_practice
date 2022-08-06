# https://www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected/
# access modifiers are of three types:
#  public
# protected
# private


# public

class PublicMod:
    def __init__(self):
        self.name #public variable

    def showName(self): #by default public
        print(self.name)

# protected 
class user:

   def __init__(self, id, name):
     self._id = id
     self._name = name

   def _userdetails(self):
     print("Id: {}, Name: {}".format(self._id, self._name))

class Employees(user):
   pass

class Emp(Employees):
    pass

e1 = Emp(1, "Suresh")
print(e1._id)
print(e1._name)
e1._userdetails()



# private

class Base:
    
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def __userdetails(self):
        print("Id: {}, Name: {}".format(self.__id, self.__name))

    def showName(self):
        print(self.__name, self.__id)
        self.__userdetails()


obj = Base("123", "mukul")

obj.showName()