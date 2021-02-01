# 스택 클래스 생성
class Stack:
  def __init__(self):
    self.stack = []
    
  def size(self):
    return len(self.stack)

  def empty(self):
    return len(self.stack) == 0

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

     
num = input()
stack = Stack()
stack.push(num)
