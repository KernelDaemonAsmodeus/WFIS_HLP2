def fibonacci():
    a = 1
    b = 0
    while True:
        c = a + b
        b = a
        a = c
        yield c


fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
