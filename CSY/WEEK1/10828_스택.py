import sys
sys.stdin=open("input.txt","rt")

def push(x):
    stack.append(int(x))
def pop():
    if len(stack)==0:
       return -1
    else:
       return stack.pop()
def size():
    return len(stack)
def empty():
    if len(stack)==0:
        return 1
    else:
       return 0
def top():
    if len(stack)==0:
        return -1
    return stack[-1]

n=int(sys.stdin.readline())
stack=[]
for _ in range(n):
    a=sys.stdin.readline().split()

    if a[0]=='push':
        push(a[1])
    elif a[0]=='pop':
        print(pop())
    elif a[0]=='size':
        print(size())
    elif a[0]=='empty':
        print(empty())
    elif a[0]=='top':
        print(top())

