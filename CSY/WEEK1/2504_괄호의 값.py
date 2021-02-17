import sys
sys.stdin=open("input.txt","rt")

s=input()
stack=[]
ss=[]
res=0


for i in s:
    if i=='(':
        ss.append(i)
    elif i=='[':
        ss.append(i)
    elif i==')':
        if not ss:
             print(0)
             exit(0)
        if ss[-1]=='(':
            ss.pop()
    elif i==']':
        if not ss:
             print(0)
             exit(0)
        if ss[-1]=='[':
            ss.pop()
if ss:
    print(0)
    exit(0)

for i in s:
    if i==')':
        tmp=0
        while stack:
            top = stack.pop()
            if top=='(':
                if tmp==0:
                    stack.append(2)
                    break
                else:
                    stack.append(2*tmp)
                    break
            elif top=='[':
                print(0)
                exit(0)
            else:
                tmp+=int(top)
    elif i==']':
        tmp=0
        while stack:
            top = stack.pop()
            if top=='[':
                if tmp==0:
                    stack.append(3)
                    break
                else:
                    stack.append(3*tmp)
                    break
            elif top=='(':
                print(0)
                exit(0)
            else:
                tmp+=int(top)
    else:
        stack.append(i)
while stack:
    res+=stack.pop()
print(res)

