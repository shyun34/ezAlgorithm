
n = int(input())
array = []

for _ in range(n):
    array.append(str(input()))

enterList = []
leaveList = []

for item in array :
   temp = item.split(' ')
   if temp[1] == 'enter':
       enterList.append(temp[0])
   else :
       leaveList.append(temp[0])

for enterItem in enterList:
    for leaveItem in leaveList:
        if leaveItem == enterItem:
            enterList.remove(enterItem)

for i in enterList:
    print(i)
