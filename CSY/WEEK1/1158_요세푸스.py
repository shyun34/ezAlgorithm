import sys
from collections import deque
sys.stdin=open("input.txt","rt")

n,k=map(int,input().split())
dq=deque()
res=[]
for i in range(1,n+1):
    dq.append(i)

while dq:
    for i in range(k-1):
        tmp=dq.popleft()
        dq.append(tmp)
    res.append(dq.popleft())
print('<'+', '.join(map(str,res))+'>')