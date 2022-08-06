class linkedlist:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
        self.head = None
    def AddNode(self, val):
        if self.head == None:
            self.head = linkedlist(val)
        else: 
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = linkedlist(val)
    def printlist(self):
        if self.head == None:
            print("linked list is empty")
            return 
        else:
            temp = self.head
            while temp.next != None:
                print(temp.value)
                temp = temp.next

a = linkedlist(9)
a.AddNode(10)
a.AddNode(20)
a.AddNode(30)
a.printlist()


        
            
