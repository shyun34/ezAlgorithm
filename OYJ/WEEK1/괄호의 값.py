#input = list(input().strip())



# 입력값이 유효한지 체크
def isValid(input):

  
  if isinstance(input, list):
    bin = []
    if len(input) % 2 != 0: return False
    if input[0] == ')' or input[0] == ']': return False
    for i in input:
      if i == '(' or i == '[': bin.append(i)
      elif i == ')':
        if bin[-1] != '(' or len(bin) == 0: return False
        else: bin.pop()
      elif i == ']':
        if bin[-1] != '[' or len(bin) == 0: return False
        else: bin.pop()
  else: return False
  return True

# 값 구하기
def getValue(input):
  calc = [0,0]
  stack = []
  val = 0

  if isValid(input):
    for i in input:
      if i == '(':
        stack.append(i)
        calc[0] += 1
      elif i == ')':
        val += 2
        
      elif i == ']':

  else: val = 0


  return val

input = list('(())')
    
#print(isValid(input))
print(getValue(input))

