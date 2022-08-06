# the act of calling function from itself is called recurssion

# to stop recursion from running infinity times we must have some base condition.
# if base condition is not there then it gives stackoverflow error.

# mathematically example of recursion
# f(x) = f(x-2) + 8  , x > 0  // recursion
# f(x) = 1           , x <= 0  // base condition



def  f(x: int) -> int:    
    if(x <= 0):
        return 1
    return f(x - 2) + 8



print(f(5))
    





