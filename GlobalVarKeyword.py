''' GLOBAL VARIABLES - Variables that are created outside of a function '''

# Declaration
# Initialisation
Calling

x = "Easy to understand"

def myfunc():
    print("Python is " + x)
    
myfunc()

# ----------------------------------------------

x = "Easy to understand"

def myfunc():
    x = "fantastic"
    print("Python is " + x) # local variable

myfunc()
print("Python is " + x) #global variable


''' Global Keyword '''
from typing import Text


def myfunc():
    global y
    y = "fantastic"
    print("Python is " + y)

myfunc()
print("Python is " + y) # Python is fantastic
