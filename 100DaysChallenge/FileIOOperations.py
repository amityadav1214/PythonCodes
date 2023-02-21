#File IO Operations
f = open("myfile.txt",'r')
text = f.read()
print(text)
f.close()

f1 = open("myfile2.txt",'w')
t1 = f1.write("Amit, Ek Number")
f1.close() #When writing to a file, we have to close the file to properly execute the write function. 

f1 = open("myfile2.txt",'a')
t1 = f1.write("Amit, Ek Number")
f1.close()

with open("myfile2.txt",'w') as f:
  f.write("Amit, Ek Number") # With clause automatically closes the file after it is written
