import re

class dictionary:
    def __init__(self):
        self.myDict = {}
        

    def addItemsInDict(self, Key, Details):
        if self.myDict.get(Key) == None:
            self.myDict[Key] = Details    
        else:    
          for i in Details:
            self.myDict[Key].append(i)
            
    def showItemInDict(self, key):
        reObj = re.compile(key)

        for keys in self.myDict.keys():
            if(reObj.match(keys)):
                print( keys, self.myDict[keys])
       

    def deleteItems(self, key):
        self.myDict.pop(key)

    def deleteAllItems(self):
        self.myDict.clear()

a = dictionary()
# a.addItemsInDict("Mayank", [9871714701,23543,2345432,2345234,43252])
# a.addItemsInDict("Mukul", [9871714701,23543,2345432,2345234,43252])
# a.showItemInDict("Muk")
# print(a.myDict)


while(True):
    print("All the available options to create a phonebook \n 1 - To add data in phonebook \n 2 - To search phonenumber by name \n 3 - Add any other phone number \n 4 - delete any record \n 5 - show all phone number\n 6 - delete all records")
    inp = int(input("Press s.no to perform any task : "))
    if (inp == 1):
        key = input("Give key name : ")
        numb = input("Give list or single value of number to add : ").split(",")
        a.addItemsInDict(key,numb)
    elif(inp == 2):
        key = input("enter the key you want to search : ")
        a.showItemInDict(key)
    elif(inp == 3 ):
        key = input("enter key which you want to update : ")
        numb = input("enter number or details you want to update : ")
        a.addItemsInDict(key, numb)
    elif (inp == 4):
        key = input("record or key you want to delete : ")
        a.deleteItems(key)
    elif(inp == 5):
        print(a.myDict)
    elif(inp == 6 ):
        a.deleteAllItems()
    else:
        print("bhai 1 se 6 tk hi h options")
        continue
