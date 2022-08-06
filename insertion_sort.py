l = [3,6,1,8,5,3,9,7,5]

def insertion_sort(list):
    l = list 
    for i in range(1, len(l)):  #iterate j
        temp = l[i]
        n = i - 1
        while n >= 0 and temp < l[n]:
                l[n + 1] = l[n]
                n = n - 1
        l[n + 1] = temp
    return l 

print(insertion_sort(l))