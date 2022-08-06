# name , age = input("enter your name and age" ).split(",")
# print("your name and age is ", name , age)
# print(f"your name is {name} and age is {age}")

lan  = "Python"
print(lan[0])  # square brackets are always used for index.

# slicing or selecting sub-sequence 
# lan[start argument: end argument]  --syntax
print(lan[0:2], lan[2:4], lan[4:6], lan[2:], lan[:4])

# steps argument syntax - lan[start : end : steps]
j = str(121)
j1 = list(j)
print(lan[0::2])
print(lan[-2])
a= []
for i in range(1,len(j1)+1):
    a.append(j1[-i])
print(j1 == a)

