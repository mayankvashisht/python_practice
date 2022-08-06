# POWER QUESTION

# k = int(input("give base : "))
# n = int(input("give power : "))
# answer = k
# for i in range(n - 1) :
#     answer = answer * k

# print("power of k to n is : ", answer)


# # FACTORIAL QUESTION
# factorial = int(input("enter factorial : "))
# answer1 = factorial
# for i in range(1,factorial):
#     answer1 = answer1 * (factorial - i)
    
# print("factorial is : ", answer1)


#PRIME NUMBER QUESTION
from sympy import N


def IsPrime(i):
    for j in range(2,i):
        if (i%j == 0 ):
            return False


    return True

arr = int(input("enter how many prime number : "))
answer2 = []
i = 2
while(len(answer2) <= arr - 1):
    isprime = IsPrime(i)
    if (isprime == True) :
        answer2.append(i)        
    i = i + 1

    
print("prime numbers - ",answer2)



# # split the input
# input1 = int(input("enter input in numbers: "))
# input1 =  str(input1)
# answer3 = []
# for i in range(1,len(input1)+1):
#     answer3.append(input1[-i])
# print("reversed ouput : ", int("".join(answer3)))

    