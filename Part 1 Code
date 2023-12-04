# Introducing things etc.
with open('puzzleInput.txt','r') as f:
  x = f.readlines()
charLis = []
totalLis = []
totalNum = 0
selection = '123456789'
selectStr = ''


# Working out the calibration numbers and final number
for i in x:
  selectStr = ''
  for a in i:
    if selection.find(a) != -1:
      selectStr += a
  thisIsANum = int(selectStr[0] + selectStr[-1])
  totalNum += thisIsANum
print(totalNum)
