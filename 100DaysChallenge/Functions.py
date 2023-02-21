#Average function with multiple arguments
def average(*numbers):     #One star represent tuple, 2 stars represent Dictionary
  sum = 0
  for i in numbers:
    sum = sum+i
  print("Average is ",sum/len(numbers))

average(10,9,91,98,28,36,84,98)