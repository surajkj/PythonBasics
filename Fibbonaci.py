# Print Fibbonaci series upto n

def fib(n):
    "Pring fib docs"
    a,b = 0,1
    while a<n:
        print(a)
        a,b = b,a+b

x = int(input('Please enter a number :\n'))
fib(x)