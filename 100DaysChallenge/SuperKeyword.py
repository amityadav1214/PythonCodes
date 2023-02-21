class Employee:
  def __init__(self,name,id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self,name,id,lang):
    super().__init__(name,id)
    self.lang = lang

e1 = Employee("Sameer",100)
print(e1.name)
print(e1.id)
e2 = Programmer("Amit",101,"Python")
print(e2.name)
print(e2.id)
print(e2.lang)
