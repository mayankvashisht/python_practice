class atm:
    def __init__(self):
        self.User_key = {}
        self.transaction = {}

    def addUserName(self, name, userID, Iamt):
        self.User_key[userID] = [name, Iamt]
        self.transaction[userID] = []

    def checkUser(self, userID):
        if (self.User_key.get(userID)):
            print("Name -",self.User_key[userID][0] ,"\n","balance -", self.User_key[userID][1] )

        else:
            print("User ID not exist")


    def balance(self, userid):
        inp = int(input("Choose - \n 1. withdraw \n 2. Deposit "))
        # useri = input("enter userid")
        amnt = int(input("Enter Amount - "))

        if ( inp == 1):
            if(amnt >= 0) and (amnt <= self.User_key[userid][1]):
                a = self.User_key[userid][1]
                b = amnt
                self.User_key[userid][1] = a - b
                self.transaction[userid].append(("DEBIT",  b ))
            elif(amnt < 0):
                print("cannot withdraw negetive amount")
            else:
                print("Not possible")
        elif(inp == 2):
            a = self.User_key[userid][1]
            b = amnt
            self.User_key[userid][1] = a +  b
            self.transaction[userid].append(("CREDIT", b ))
        else:
            print("Wrong Selection")

a = atm()

while(True):
    print("Select the options \n1. Add user \n2. check User \n3. Do transactions \n4. show all transactions")
    inpu = int(input())
    if (inpu == 1 ):
        inp1 = input("Username : ")
        inp2 = input("UserId : ")
        inp3 = int(input("Initial Balance : "))
        a.addUserName(inp1,inp2,inp3)
    elif(inpu == 2):
        inp_userid = input("enter user ID : ")
        a.checkUser(inp_userid)
    elif(inpu == 3):
        inp_bal = input("Enter you userID : ")
        print(a.balance(inp_bal))
    elif(inpu == 4):
        inp5 = input("enter user id : ")
        for i in range(0, len(a.transaction[inp5])):
            print(a.transaction[inp5][i])

    else:
        print("wrong input")
    
