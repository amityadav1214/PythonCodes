marks = [23,45,67,47,57,87,76,28]
for index,mark in enumerate(marks):
  print(index,mark)
  if index == 5:
    print("Good Score, Amit")

#Starting Index
for index,mark in enumerate(marks, start = 1):#Can write it in tuple format as well
  print(index,mark)
  if index == 6:
    print("Good Score, Amit")
