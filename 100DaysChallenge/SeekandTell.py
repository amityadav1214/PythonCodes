#Seek and Tell Function
with open("myfile3.txt",'r') as f:
  f.seek(10)
  curr_pos = f.tell()
  data = f.read(5)
  print(data)
  print(curr_pos)
