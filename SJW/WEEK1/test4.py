n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = sorted(array)

for i in array:
    print(i)