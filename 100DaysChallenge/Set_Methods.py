#Sets
amit = set()  #Empty Set
print(type(amit))

amit = {1,2,3,"amit"}
for value in amit:
  print(value)

#Set Methods
s1 = {1,3,5,7,6}
s2 = {1,2,4,6,8}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s2)
print(s1)
s3 = {1,3,5,7,6}
print(s3)
s3.intersection_update(s2)
print(s3)
print(s2.symmetric_difference(s3))
print(s2.difference(s3))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
s3.add(9)
print(s3)
s3.remove(9)
print(s3)
s3.discard(9)
print(s3)
s3.add(9)
print(s3)
s3.pop()
print(s3)
s3.clear() #will clear the set
print(s3)
del s3 #Will delete whole set
print(s3)

