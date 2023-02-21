#Import Module Usage
import math
print(math.floor(4.223123))

#We can only import certain packages from whole module.This reduces complexity in big programs and is good practice
from math import sqrt,pi,floor
a= floor(sqrt(9) * pi)
print(a)

#We can give alias which can be used in further programs
import math as m
print(m.floor(4.223123))

#dir function: Gives Function in particular module
import math as m
print(dir(m))
print(m.nan,type(m.nan))
