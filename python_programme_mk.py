
print("Sun be, type kar konsa data type ya data structure chaahiye. Niche mese koisa bhi select krle :")
print(" 1. Integer\n 2. Float \n 3. String\n 4. List\n 5. Tuple \n 6. Set ")

def Integer():
    print("Tere pass yeh sab methods h choose kr konsa chahiye(to choose any method type s.no. of operations listed below.) : \n1. guda(Multiply)\n2. bhag(Divide)\n3. Power ")
    inp = int(input())
    val = input("input numbers that you want to multiply(separated by commas)").split(",")
    if(inp == 1):
        # Numbval = input("how many values you want to multiply")
        print(int(val[0])*int(val[1]))
    elif(inp == 2):
        print(int(val[0])/int(val[1]))
    elif(inp == 3):
        print(int(val[0]) ** int(val[1]))
    else:
        print("You can only select 1, 2 or 3! Bewakoof!!!")

def Float():
    print("Tere pass yeh sab methods h choose kr konsa chahiye(to choose any method type s.no. of operations listed below.) : \n1. guda(Multiply)\n2. bhag(Divide)\n3. Power ")
    inp = int(input())
    val = input("input numbers that you want to multiply(separated by commas)").split(",")
    if(inp == 1):
        # Numbval = input("how many values you want to multiply")
        print(float(val[0])*float(val[1]))
    elif(inp == 2):
        print(float(val[0])/float(val[1]))
    elif(inp == 3):
        print(float(val[0]) ** float(val[1]))
    else:
        print("You can only select 1, 2 or 3! Bewakoof!!!")

def String():
    print("Tere pass yeh sab methods h choose kr konsa chahiye(to choose any method type s.no. of operations listed below.) : \n1. do string jod do\n2. ek string ko n bar likho\n3. remove duplicates ")
    inp = int(input())
    val = input("input numbers that you want to apply method on(separated by commas)").split(",")
    if(inp == 1):
        # Numbval = input("how many values you want to multiply")
        print(val[0] + val[1])
    elif(inp == 2):
        print(val[0] * int(val[1]))
    elif(inp == 3):
        print(set(val[0]), set(val[1]))
    else:
        print("You can only select 1, 2 or 3! Bewakoof!!!")

def List():
    val = input("Enter all the element jo add krna chahta h list me(comma separated):").split(",")
    print("This is your list \n", val)
    print("Tere pass yeh sab methods h choose kr konsa chahiye(to choose any method type s.no. of operations listed below.) : \n1. append \n2. change the element at nth position \n3. view element at ith and jth index ")
    inp = int(input("enter s.no. of method : "))
    if (inp == 1):
        a = input("type strings you want to add to the list(comma separated) : ").split()
        val.append(a)
        print("This is your list ",val)
    elif (inp == 2):
        b = int(input("enter index of element you want to replace : "))
        c = input("enter the character you want to replace it with : ")
        val[b] = c
        print("this is your list now : ", val)
    elif (inp == 3):
        i = int(input("enter starting index and end index : ").split(","))
        print("this is your list indexed from ",i[0], " to ",i[1]," - \n", val[i[0],i[1]] )

    else:
        print("You can only select 1, 2 or 3! Bewakoof!!!")

def Set():
    val = set(input("Enter all the element jo add krna chahta h set me(comma separated):").split(","))
    print("This is your set \n", val)
    print("Tere pass yeh sab methods h choose kr konsa chahiye(to choose any method type s.no. of operations listed below.) : \n1. add \n2. clear all the elements ")
    inp = int(input("enter s.no. of method : "))
    if (inp == 1):
        a = input("type strings you want to add to the list(comma separated) : ").split()
        val.set(a)
        print("This is your list ",val)
    elif (inp == 2):
        val.clear()
        print("this is your list now : ", val)
    else:
        print("You can only select 1, 2 or 3! Bewakoof!!!")
# while (true ):

def Tuple():
    val = input("enter the input you want to add in the tuple : ").split()
    print("this is your tuple " , tuple(val))

while (True):
    i = int(input("to select the data type, type the s.no. of data type listed above : "))
    if (i == 1):
        Integer()
    elif(i == 2):
        Float()
    elif(i == 3):
        String()
    elif(i == 4):
        List()
    elif(i == 5 ):
        Tuple()
    elif(i == 6):
        Set()
    else:
        print("abe pagal admi 1 se 6 tk koi select krna buddu!!!!")