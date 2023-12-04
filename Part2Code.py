# Introducing things etc.
with open('puzzleInput.txt','r') as f:
  x = f.readlines()
charLis = []
totalLis = []
totalNum = 0
selection = '123456789'
selectStr = ''


# Editing the string to account for the numbers written as words
for i in x:
  temp = i.replace('one','one1one')
  temp = temp.replace('two','two2two')
  temp = temp.replace('three','three3three')
  temp = temp.replace('four','four4four')
  temp = temp.replace('five','five5five')
  temp = temp.replace('six','six6six')
  temp = temp.replace('seven','seven7seven')
  temp = temp.replace('eight','eight8eight')
  temp = temp.replace('nine','nine9nine')
  charLis.append(temp)


# Working out the calibration numbers and final number
for i in charLis:
  selectStr = ''
  for a in i:
    if selection.find(a) != -1:
      selectStr += a
  thisIsANum = int(selectStr[0] + selectStr[-1])
  totalNum += thisIsANum
print(totalNum)
