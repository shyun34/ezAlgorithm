import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a={}
for i in range(n):
    log=input().split()
    if log[1]=='enter':
        a[log[0]]=1
    else:
        a[log[0]]=0
for k,v in a.items():
    if v==1:
        print(k)
