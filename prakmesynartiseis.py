def zero(f=None): #default timi h null
    if f is None:
        return 0
    return f(0)
    

def one(f=None): 
    if f is None:
        return 1
    return f(1)
    
    
def two(f=None): 
    if f is None:
        return 2
    return f(2)
    

def three(f=None): 
    if f is None:
        return 3
    return f(3)
    

def four(f=None): 
    if f is None:
        return 4
    return f(4)
   

def five(f=None): 
    if f is None:
        return 5
    return f(5)
    

def six(f=None): 
    if f is None:
        return 6
    return f(6)
    

def seven(f=None): 
    if f is None:
        return 7
    return f(7)
    
def eight(f=None): 
    if f is None:
        return 8
    return f(8)
    

def nine(f=None): 
    if f is None:
        return 9
    return f(9)
    

def plus(x):
    return  lambda y: y + x

def minus(x):
    return  lambda y: y - x

def times(x):
    return  lambda y: y * x
