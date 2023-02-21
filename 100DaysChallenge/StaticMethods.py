#Static Methods
class Maths:
  def __init__(self,num):
    self.num = num
  def addtonum(self,n):
    self.num = self.num + n
  @staticmethod
  def add(a,b):
    return a + b

a = Maths(5)
print(a.num)
a.addtonum(4)
print(a.num)
print(a.add(4,9))
print(Maths.add(4,9)) #Can be called in this way as well
#With Static Method Decorator we dont need to declare self in methods of the class
