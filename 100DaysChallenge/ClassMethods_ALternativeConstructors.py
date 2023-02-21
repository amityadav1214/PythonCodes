#Class Methods as Alternative Constructors
class Employee:
  def __init__(self,name, salary):
    self.name = name
    self.salary = salary
  @classmethod
  def fromstr(cls,string):
    return cls(string.split("-")[0],string.split("-")[1])

e1 = Employee("Harry",12000)
print(e1.name)
print(e1.salary)

string = "Amit-100000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)

#We can use class methods as alternative constructors to get spefific format data from our class itself
