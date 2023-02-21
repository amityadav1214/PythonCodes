#Access Modifiers
#Public Modifiers
class Employee:
  def __init__(self):
    self.name = "Amit"

a= Employee()
print(a.name)

#Private Modifiers
class Employee:
  def __init__(self):
    self.__name = "Amit"

a= Employee()
#print(a.__name) #Will not work as now __name has become Private object in class.
print(a._Employee__name) #But still private specifiers can be accessed like this indirectly. Also called as Name Mangling

#Protected Modifiers
class Employee:
  def __init__(self):
    self._name = "Amit"

a= Employee()
print(a._name) #Protected Work with Single Underscore
