#Operator Overloading
class Vector:
  def __init__(self,i,j,k):
    self.i = i
    self.j = j
    self.k = k
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
  def __add__(self,x):#Remember use Dunder method to get the actual type of its class
    return Vector(self.i+x.i,self.j+x.j,self.k+x.k)

v1= Vector(3,4,9)
print(v1)
v2= Vector(5,6,8)
print(v2)
print(v1+v2)
