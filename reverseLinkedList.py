# WAP to reverse a linked list without using recursion.

# https://leetcode.com/problems/reverse-linked-list/
# mann kare toh submit bhi kardiyo pehele yaha kariyo

# https://leetcode.com/problems/add-two-numbers/ - do at your own pace after first question above
class node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
class linked:
    def __init__(self) -> None:
        self.head = None
    def add_node(self,val):
        if self.head == None :
            self.head = node(val)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node(val)
    def print_node(self):
        if self.head == None:
            print("No nodes")
        else:
            arr = []
            temp = self.head
            while temp.next != None:
                arr.append(temp.val)
                temp = temp.next
            arr.append(temp.val)
            print(arr)

    def reverse_link(self):
        if self.head == None:
            print("there is no node")
        else:
            arr = []
            temp = self.head
            while temp.next != None:
                arr.append(temp.val)
                temp = temp.next
            arr.append(temp.val)   
            temp = self.head
            i = len(arr) - 1
            while temp.next != None:
                temp.val = arr[i]
                temp = temp.next
                i = i - 1

    def reverse_wo_list(self):
        if self.head == None:
            print("node is empty")
        else:
            temp_curr = self.head
            temp_next = None
            temp_prev = None
            while temp_curr.next != None :
                temp_next = temp_curr.next
                temp_curr.next = temp_prev
                temp_prev = temp_curr
                temp_curr = temp_next
            self.head = temp_prev
                    




a = linked()
a.add_node(2)
a.add_node(4)
a.add_node(6)
a.add_node(8)
a.add_node(12)
a.print_node()
a.reverse_link()
a.print_node()
a.reverse_wo_list()
a.print_node()