##Interactive Caluclator
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = input("Choose operators from (+,-,/,*,%,**) for calculations")
if c == "+":
  print("Addition of ", a, " and ", b, "is: ", a + b)
if c == "-":
  print("Substraction of ", a, " and ", b, "is: ", a - b)
if c == "*":
  print("Multiplication of ", a, " and ", b, "is: ", a * b)
if c == "/":
  print("Division of ", a, " and ", b, "is: ", a / b)
if c == "**":
  print("Exponential of ", a, " to the power of ", b, "is: ", a**b)
if c == "%":
  print("Modulus of ", a, " and ", b, "is: ", a % b)

##Factorial of a Number
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(19))
