#Time Module
import time
def usingWhile():
  i = 0
  while(i<10000):
    print(i)
    i = i+1
def usingFor():
  for i in range(10000):
    print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

#sleep
print(4)
time.sleep(5)
print("Run after 5 seconds")

#strftime
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)
