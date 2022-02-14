def fib(n):
    n1 = 0
    n2 = 1
    addition = n1 + n2
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
         for i in range(2, n):
            num = n1 + n2
            addition += num
            n1 = n2
            n2 = num
         return addition

print(fib(5))
print(fib(10))