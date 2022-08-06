# singly linked list
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNode(self,val):
        if self.head == None:
            self.head = Node(val)

        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next

            temp.next = Node(val)

    def delete(self, index):
        i = 0
        prev = None
        curr = self.head
        if index == 0:
            self.head = curr.next
            del curr 
            return
            
        while i != index and curr != None :
            prev = curr
            curr = curr.next
            i = i + 1
        if curr != None and index != 0 :
            prev.next = curr.next 
            del curr  

        # 14 -> 65-> 343 ->24
        #prev = 343
        #curr = 24
        # i = 3
        #   


    def findMiddleOfLinkedListUsingTwoPointer(self):
        temp_fast = self.head
        temp_slow = self.head
        while temp_fast.next != None and temp_fast.next.next != None:
            temp_fast = temp_fast.next
            temp_fast = temp_fast.next
            temp_slow = temp_slow.next
        print(temp_slow.val)
# 1->23->34->3


    def traverseLinkedListUsingRecursion(self):
        self.travLL(self.head)
        print()

    def travLL(self, node):
        if node == None:
            return
        print(node.val, end=" -> ")
        return self.travLL(node.next)


    def printLLInRevers(self):
        self.travLLRev(self.head)
        print()

    def travLLRev(self, node):
        if node == None:
            return
        
        self.travLLRev(node.next)
        print(node.val, end=" -> ")
        return


    def reverseLLUsingRec(self):
        self.reverseLL(self.head)

    def reverseLL(self, node):
        if node.next == None:
            self.head = node
            return node

        aageValaNode = self.reverseLL(node.next)
        aageValaNode.next = node
        node.next = None
        return node
        



    def printLinkedList(self):
        if self.head == None:
            print("linked list is empty")
            return

        temp = self.head
        while(temp != None):
            print(temp.val, end=" -> ")
            temp = temp.next
        print()

mylist = LinkedList()

# mylist.printLinkedList()
mylist.addNode(10)
mylist.addNode(90)
mylist.addNode(1900)
mylist.addNode(23423)
mylist.addNode(500)
# mylist.addNode(1)

mylist.printLinkedList()
# # mylist.delete(0)
# mylist.printLinkedList()
# mylist.findMiddleOfLinkedListUsingTwoPointer()
# mylist.traverseLinkedListUsingRecursion()
# mylist.printLLInRevers()
mylist.reverseLLUsingRec()
mylist.printLinkedList()
#       10 -> 5 -> 9 -> 11 -> 12 -> 17 -> 18



# a = node()


# 12 -> 10 -> 13 -> 14
# 14 -> 13 -> 10 -> 12

