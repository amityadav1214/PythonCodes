#Class Methods
class Employee:
  company  = "Apple"
  def show(self):
    print(f"Hello I am {self.name} and I am from {self.company}")
  @classmethod #Using Class method decorator we can assign value to class variable through instance
  def changeCompany(cls,newCompany):
    cls.company = newCompany

a = Employee()
a.name= "Amit"
a.show()
a.changeCompany("Tesla")
a.show()
print(Employee.company)    
