#input = list(input().strip())



# 입력값이 유효한지 체크
def isValid(input):

  res = True
  if isinstance(input, list):
    bin = []
    if len(input) % 2 != 0: res = False
    if input[0] == ')' or input[0] == ']': res = False
    for i in input:
      if i == '(' or i == '[': bin.append(i)
      elif i == ')':
        if bin[-1] != '(' or len(bin) == 0: res = False
        else: bin.pop()
      elif i == ']':
        if bin[-1] != '[' or len(bin) == 0: res = False
        else: bin.pop()
  else: res = False
  return res

# 값 구하기
def getValue(input):
  a = []
  b = []
  stack = []
  val = 0

  if isValid(input):
    for i in input:
      if i == '(' or i == '[':
        stack.append(i)
      elif i == ')':
        
      elif i == ']':

  else: val = 0

  return val

input = list('(())')
    
#print(isValid(input))
print(getValue(input))

