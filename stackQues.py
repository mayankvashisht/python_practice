# WAP to verify if given sequence of brackets is correct or not
# for ex:
#  input - "()"
#  return - true
#   input - ")("
#   return - false
#  input - "(()"
#  return - false

from stack import *


mystack = Stack()
inp = list(input())



for i in inp:
    if i == ')' and mystack.top() ==  '(':
        mystack.pop()
    else:
        mystack.push(i)

if mystack.isEmpty():
    print("equation is correct")

else:
    print("equation is not correct")    

