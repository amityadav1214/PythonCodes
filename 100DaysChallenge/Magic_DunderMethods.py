class Employee:

  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Hi I am {self.name}"

  def __repr__(self):
    return f"Hi I am {self.name}!!Nice to meet you"

  def __call__(self,a,b):
    return a**b

  def __len__(self):
    return len(self.name)


from emp import Employee
e = Employee("Amit")
print(str(e))
print(repr(e))
print(len(e))
print(e(2,3))
