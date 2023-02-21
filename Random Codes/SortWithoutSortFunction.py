list1 = [20,30,12,13,12,38,49,25]
#print(type(list1))
n=len(list1)
for i in range(n):
    for j in range(i+1,n):
        if list1[i]>list[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)
