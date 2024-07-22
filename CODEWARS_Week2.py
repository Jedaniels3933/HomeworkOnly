#CODEWARS 

#Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".
#I can do math on numbers only
# #typecast a
# a = int(a)    This fails if a is not a number
#typecast to string

def problem(a):
    if a == str(a):
        return "Error"
    
    return (a * 50) + 6  

