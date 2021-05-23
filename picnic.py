def printPicnic(itemsDict, leftWidth, rightWidth):
  print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
  for k, v in itemsDict.items():
    print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidht))

picnicItems = {}
