# 스택 클래스 생성
class Stack:
  def __init__(self):
    self.top = []
    
  def size(self):
    return len(self.top)

  def empty(self):
    return len(self.top) == 0

  def push(self, item):
    self.top.append(item)

  def pop(self):
    if not self.empty():
      return self.top.pop(-1)
    else:
      return -1

  def top(self):
    if not self.empty():
      return self[-1]
    else:
      return -1