# 1. Functions
"""


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial(3))
print(factorial(5))

##############################

def max(a, b):
    
    if a > b:
        return a
    else:
        return b

print(max(3, 5))
print(max(5, 3))
print(max(int(input()), int(input())))

#############################


def max(a, b):
    
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    return max(max(a, b), c)

print(max3(3, 5, 4))






####################################




def max(*a):
    res = a[0]
    for val in a[1:]:
        if val > res:
            res = val
    return res

print(max(3, 5, 4,7,8,9))
"""

# 2. Local and global variables

"""
def f():
    print(a)

a = 1
f()   #1

################


def f():
    a = 1

f()
print(a) #Error

#############
def f():
    a = 1
    print(a)

a = 0
f()
print(a)  #1 0

################

def f():
    print(a)
    if False:
        a = 0

a = 1
f()  # Error. local variable 'a' referenced before assignment

############


def f():
    global a
    a = 1
    print(a)

a = 0
f()
print(a) # 1 1

####################
def factorial(n):
    global f
    res = 1
    for i in range(2, n + 1):
        res *= i
    f = res

n = int(input())
factorial(n)
print(f)  
######################

# start of chunk of code that can be copied from program to program
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
# end of piece of code

n = int(input())
f = factorial(n)
print(f)
# doing other stuff with variable f
"""

# 3. Recursion

"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

###################


"""