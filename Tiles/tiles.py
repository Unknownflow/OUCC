import math
leng = int(input())
width = int(input())
edge = float(input())

print(math.ceil(leng / edge) * math.ceil(width / edge))
