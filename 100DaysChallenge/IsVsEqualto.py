a=3
b=3
print(a is b)# checks exact location in the memory
print(a == b)# checks values

c = [1,2,3]
d = [1,2,3]
print(c is d)#For lists python create different memory for each list as lists are mutable objects. It works differently for tuples
print(c == d)
