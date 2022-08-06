# A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
#  This means the last element inserted inside the stack is removed first.
# You can think of the stack data structure as the pile of plates on top of another.


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False     

    def push(self, val):
        self.stack.append(val)
    

    def pop(self):
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return
        return self.stack[-1]



