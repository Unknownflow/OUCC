choice = input()
msg = input()

if choice == 'encode':
  msglist = []
  encodedmsg = ''
  
  for i in range(len(msg)):
    if i % 4 == 0:
      msglist.append([])
    msglist[-1] += msg[i]
  
  while len(msglist[-1]) != 4:
    msglist[-1] += 'x'
    
  for i in range(4):
    for j in range(len(msglist)):
      encodedmsg += msglist[j][i]
  
  print(encodedmsg.upper())
  
else:
  msglist = []
  decodedmsg = ''
  num = len(msg) // 4
  for i in range(len(msg)):
    if i % num == 0:
      msglist.append([])
    msglist[-1] += msg[i]
    
  for i in range(num):
      for j in range(len(msglist)):
        decodedmsg += msglist[j][i]
  
  print(decodedmsg.lower())
