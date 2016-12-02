p = int(input())
def fib(n,a,b):
    if n == 1:
        if a > b:
            return b
        else:
            return a
    else:
        if n % 2== 0:
            a +=  b
            return fib(n-1,a,b)
        else:
            b += a
            return fib(n-1,a,b)
print(fib(p,1,1))