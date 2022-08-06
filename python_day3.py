# methods and functions - the function which we used as variable.function such as variable.upper() is methods 
# but when we use arguments inside it then it is function such as len(variable).

name = "MaYank VasHiShT"

print(len(name) , name.upper() , name.lower() , name.title(), name.count("a")) 

# to remove the space from string use lstrip, rstrip and strip and replace to replace space with no space.

nam = "      mayank     "
print(nam.lstrip())
print(nam.rstrip())
print(nam.strip())
print(nam.replace(" ",""))
