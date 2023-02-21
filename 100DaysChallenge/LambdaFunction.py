#Lambda Function
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/2
print(cube(2))
print(avg(5,10,20))

def appl(fx,value):
  return fx(value)

print(appl(cube,7))
print(appl(lambda x: x*x,6))# Lambda Func passed as an argument
