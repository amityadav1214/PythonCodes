#Recursion
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(4))
print(factorial(7))
print(factorial(6))


#Fibonacci Sequence
def fib(n):
  if (n == 0 or n == 1):
    return n
  else:
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(10)])
