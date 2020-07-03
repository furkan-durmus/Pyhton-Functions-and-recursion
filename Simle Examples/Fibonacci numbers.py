# Given a non-negative integer n, print the nth Fibonacci number.
# Do this by writing a function fib(n) which takes the non-negative integer n and returns the nth Fibonacci number.
# Don't use loops, use the flair of recursion instead.
# However, you should think about why the recursive method is much slower than using loops.
c=1
temp=0
def fibonacci(a):
    global c,temp
    if a==0:
        return 0
    else:
        c,temp=temp+c,c
        fibonacci(a-1)
        return temp
print(fibonacci(int(input())))
