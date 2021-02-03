import sys
sys.stdin=open("input.txt","rt")

#bubble sort

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
for i in a:
    print(i)