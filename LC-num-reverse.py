def reverse(x):
  x = str(x)
  newstr = []
  rev = []
  for char in x:
    newstr.append(char)
  
  if newstr[0] == '-':
    newstr.pop(0)
    if newstr[0] == 0:
      newstr.pop(0)
    else:
      while(newstr):
        rev.append(newstr.pop())
    final = "".join(rev)
    final = int(final)
    final = final * (-1)
  else:
    if newstr[0] == 0:
      newstr.pop(0)
    else:
      while(newstr):
        rev.append(newstr.pop())
      
      final = "".join(rev)
      final = int(final)    

  print(final + 1)
  

reverse(int(input("")))