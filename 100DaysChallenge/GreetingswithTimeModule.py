import datetime,time
currentTime = int(time.strftime('%H'))   
print(currentTime)
if currentTime <= 12 :
     print('Good morning')
elif 12 < currentTime <= 16 :
     print('Good afternoon')
else:
     print('Good evening')
