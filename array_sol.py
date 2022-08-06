given_arr = [3,5,6,7,7,3,5,78,-50,4]
max_arr = given_arr[0]
for i in range(len(given_arr)-1):
    if (given_arr[i+1] < max_arr  ):
        continue
    elif(given_arr[i+1] > max_arr):
        max_arr = given_arr[i+1]
    
    
print("max = ", max_arr)
min_arr= given_arr[0]
for i in range(len(given_arr) - 1):
    if (given_arr[i+1] > min_arr):
        continue
    elif(given_arr[i+1] < min_arr):
        min_arr = given_arr[i+1]
   

print("min = ", min_arr)


max_arr1 = given_arr[0]
max_arr_k = [given_arr[0]]
for i in range(len(given_arr)-1):
    if (given_arr[i+1] < max_arr1 ):
        continue
    elif(given_arr[i+1] > max_arr1):
        max_arr1 = given_arr[i+1]
        max_arr_k.append(given_arr[i+1])
    elif(given_arr[i+1] == max_arr1):
        continue
inp = int(input("enter the Kth max no. you want : "))
print("max at", inp , " is ", max_arr_k[-inp])

min_arr1= given_arr[0]
min_arr_k = [given_arr[0]]
for i in range(len(given_arr) - 1):
    if (given_arr[i+1] > min_arr1):
        continue
    elif(given_arr[i+1] < min_arr1):
        min_arr1  = given_arr[i+1]
        min_arr_k.append(given_arr[i+1])
    elif(given_arr[i+1] == min_arr1):
        continue

inp1 = int(input("enter the Kth min no. you want : "))
print("min at", inp , " is ", min_arr_k[-inp1])


k = int(input("enter K for rotation : "))
empty = []
for i in range(k,len(given_arr)):
    empty.append(given_arr[i])

for i in range(k):
    empty.append(given_arr[i])

print("with using empty list : ", empty)

n = 10, k = 5

k%n = 5

k = 11  n = 10

k % n = 1

for i in range(k):
    aside = given_arr[0]
    for i in range(len(given_arr) - 1):
        given_arr[i] = given_arr[i+1]
    given_arr[len(given_arr)-1] = aside

print("rotation without list : ", given_arr)