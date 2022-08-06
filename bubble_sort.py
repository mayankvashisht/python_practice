l = [9,9,7,230 , 6,5,0,4,3,2,1]

def bubble_sort(l:list) -> list:
    array = l

    for i in range(len(array) - 1):
        for n in range(len(array) - 1):
            if array[n] > array[n + 1]:
                array[n+1], array[n] = array[n], array[n+1]
                # temp = array[n + 1]
                # array[n + 1] = array[n]
                # array[n] = temp 
    return array

print(bubble_sort(l))



# for integers there are various ways to swap

# x = 10
# y = 20

# x = x+y
# y = x - y
# x = x - y
# print(x, y)
# print(int('a'), int('A'))



