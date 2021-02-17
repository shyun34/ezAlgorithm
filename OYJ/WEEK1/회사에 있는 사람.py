import sys

num = int(sys.stdin.readline())
employee = {}

for _ in range(num):
  name, action = sys.stdin.readline().split()
  if action == 'enter':
    employee[name] = 'enter'
  elif action == 'leave':
    if employee[name]: del employee[name]

for e in sorted(employee, reverse=True):
  print(e)