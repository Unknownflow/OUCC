sent = input()
words = sent.split(' ')
newWords = []
for word in words:
  if word[0] == 'S' or word[-1] == 'S':
    newWords.append(word[::-1].lower())
  else:
    newWords.append(word.lower())
    
print(' '.join(newWords))
