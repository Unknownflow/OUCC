digits = (input())
odds = 0
evens = 0

for i in range(0, len(digits)):
  if i % 2 == 0:
    odds += int(digits[i])
  else:
    evens += int(digits[i]) * 3
    
remainder = (odds + evens) % 10
if remainder == 0:
  print(0)
else:
  print(10-remainder)
