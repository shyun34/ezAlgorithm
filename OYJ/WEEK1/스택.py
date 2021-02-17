import sys

# 스택 클래스 생성
class Stack:
  def __init__(self):
    self.stack = []
    
  def size(self):
    return len(self.stack)

  def empty(self):
    return 1 if len(self.stack) == 0 else 0

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if not self.empty():
      return self.stack.pop(-1)
    else:
      return -1

  def top(self):
    if not self.empty():
      return self.stack[-1]
    else:
      return - 1

 # 시간초과로 input() ->  sys.stdin.readline()으로 바꿔줌   
num = int(sys.stdin.readline())
stack = Stack()
while num > 0:
  
  command = list(sys.stdin.readline().strip().split(" "))

  if command[0] == "push": stack.push(int(command[1]))
  elif command[0] == "pop": print(stack.pop())
  elif command[0] == "size": print(stack.size())
  elif command[0] == "empty": print(stack.empty())
  elif command[0] == "top": print(stack.top())

  num -= 1


