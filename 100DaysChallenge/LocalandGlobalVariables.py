#Local and Global Variables
x = 4 # Global Variable
def variab():
  global x #Declare Global Variable for the whole program beyond Function
  x=5
  print(f"The local x is: {x}")

variab()
print(f"The global x is: {x}")
