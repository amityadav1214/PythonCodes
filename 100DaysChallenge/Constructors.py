#Constructors
#Constructors always get called when object is created of a class
class Person:
  def __init__(self,n,o):
    print("I am a constructor")
    self.name = n
    self.occ = o
  def info(self):
    print(f"{self.name} is a {self.occ}")

a = Person("Amit","Developer")
b = Person(1,2,3)#not work as it has 4 arguments including self
c= Person()#not work as it needs to have 2 arguments 
a.info()
b.info()
c.info()
