import sys

num = int(sys.stdin.readline())
numList = []
for _ in range(num):
  n = int(sys.stdin.readline())
  numList.append(n)

numList.sort() 
for n in numList:
  print(n)