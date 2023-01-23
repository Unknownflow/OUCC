N = int(input())
M = int(input())
V = int(input())
first = N*(M+V)
second = M*(N+V)
third = V*(N+M)
if first > second and first > third:
  print(first)
elif second > third:
  print(second)
else:
  print(third)
