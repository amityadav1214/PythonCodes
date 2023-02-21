#Method Overriding
class Shape:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def area(self):
    return self.x * self.y


class Circle(Shape):

  def __init__(self, radius):
    self.radius = radius
    super().__init__(radius, radius)

  def area(self):
    return 3.14 * super().area()


# a = Shape(2,3)
# print(a.area())

b = Circle(3)
print(b.area())
#This is a very wrong example but a way to understand Method overriding in Child Class from Parent class method
