#Map, Filter and Reduce Functions
def cube(x):
  return x*x*x

l = [1,3,5,7,9]
# newl = []
# for items in l:
#   newl.append(cube(items))

newl = list(map(cube,l))
print(newl)
#Both above suits gives the same output

def filter_func(a):
  return a > 4
fil = list(filter(filter_func,l))
print(fil)

from functools import reduce
red = reduce(lambda x,y:x+y , l)
print(red)
