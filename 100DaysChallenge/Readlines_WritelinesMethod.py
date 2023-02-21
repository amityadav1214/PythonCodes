#Readlines
f =open("myfile2.txt",'r')
i=0
while True:
  i+=1
  line = f.readline()
  if not line:
    break
  m1 = line.split(",")[0]
  m2 = line.split(",")[1]
  m3 = line.split(",")[2]
  print(f"Marks of Student {i} in Maths is: {m1}")
  print(f"Marks of Student {i} in English is: {m2}")
  print(f"Marks of Student {i} in Science is: {m3}")


#Writelines
f= open("myfile3.txt",'w')
lines = ["Hi Amit, You are awesome!!!!!","Hi Sameer, You are awesome!!!!!","Hi Shiv, You are awesome!!!!!"]
for line in lines:
  if not line:
    break
  f.writelines(line+'\n')
f.close()
