#Exception Handling
a= input("Enter the number: ")
print(f"Multiplication of {a} is:")
try:
  for i in range(1,13):
    print(f"{int(a)} X {i} = {int(a) * i}")
except:
  print("Invalid Input!!!!")
print("Some imp lines of code")
print("End of program")

try:
  a=int(input("Enter the number: "))
  b = [6,3]
  print(b[a])
except ValueError:
  print("Vaslue is not an integer")
except IndexError:
  print("Index out of bound error")
except:
  print("Invalid Syntax")

#Finally
try:
  a=int(input("Enter the number: "))
  b = [6,3]
  print(b[a])
except ValueError:
  print("Value is not an integer")
except IndexError:
  print("Index out of bound error")
finally:
  print("Invalid sytax")

  #Custom Errors
salary = input("Enter your Salary Amount: ")
if str(salary) == "quit":
  quit
elif 2000 < int(salary) < 8000:
  raise ValueError("Not a Valid Salary")
else:
  print("Your Salary amount is: ", salary)
