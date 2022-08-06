a = [1,2,3]


a = [], capacity = 1, size = 0
a.append(2)
a = [2],  capacity = 1, size = 1
a.append(3)

internally, take new block of memory from the heap (here defines pool of memory) of size 2 and copies
element of a into that and assign to a and at given position fills with given value  
a = [2,3] , capacity = 2, size = 2

a.append(4)
a =  [2, 3, 4 ] , capacity = 4 , size = 3

a.append()


