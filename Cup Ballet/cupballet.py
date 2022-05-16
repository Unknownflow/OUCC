numCups = int(input())
numSwaps = int(input())
pos = numCups - 1

for i in range(numSwaps):
  a, b = input().split(' ')
  a = int(a)
  b = int(b)
  if a == pos:
    pos = b
  elif b == pos:
    pos = a
    
print(pos)
