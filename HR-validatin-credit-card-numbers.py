def checker(cardnumber):
  first_digit = '456'
  if cardnumber[0] not in first_digit:
    return 'Invalid'
  else:
    if len(cardnumber) != 16:      
      if '-' in cardnumber:
        if  len(cardnumber) != 19:
          return 'Invalid'
        else:
          hyp = cardnumber.split('-')
          for groups in hyp:
            if len(groups) != 4:
              return 'Invalid'
          newcard = ''
          for group in hyp:
                newcard += group                
          adjacent = 1
          for i in range(1,len(newcard)):
            if newcard[i] == newcard[i-1]:
              adjacent+=1
              if adjacent>=4:
                return 'Invalid'
            else:
              adjacent = 1
          return 'Valid'
      return 'Invalid'
    else:
      adjacent = 1
      for i in range(1,len(cardnumber)):
        if cardnumber[i] == cardnumber[i-1]:
          adjacent+=1
          if adjacent>4:
            return 'Invalid'
        else:
          adjacent = 1
      return 'Valid'


n = int(input())
cardnumbers = []
for i in range(n):
  a = input()
  print(checker(a))
