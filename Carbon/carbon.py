N = int(input())
D = int(input())

print(30*N*D)

if N % 4 == 0:
  numCar = N // 4
else:
  numCar = N // 4 + 1
numPassenger = N - numCar
print(100*numCar*D + 10*numPassenger*D)

if D >= 100:
  print(240*N*D)
else:
  print("no flight available")
