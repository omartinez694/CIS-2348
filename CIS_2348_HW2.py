#a
variable = 1
months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']
while variable == 1:
  try: #using try to test the code and except as well
    string = input("Enter the month day, year: ")
  except SyntaxError:
    continue
  if string == '-1':
    break

  try:
    arr = string.split()
    digit = len(arr)
    if digit != 3:
      continue
    m = arr[0]
    day = arr[1]
    y = arr[2]
    d, comma = day.split(',')

    for x in range(12):
      if string.find(months[x]) >= 0:
        mo = str(x+1)
        ans = mo + '/' + d + '/' + y
        print(ans)
        break
  except ValueError:
    continue
#b
file1 = open('inputDates.txt''r')
dates = file1.readlines()

months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']
for string in dates:
  if string == '-1':
    break
  try:
    arr = string.split()
    digit = len(arr)
    if digit != 3:
      continue
    m = arr[0]
    day = arr[1]
    y = arr[2]
    d, comma = day.split(',')

    for x in range(12):
      if string.find(months[x]) >= 0:
        mo = str(x + 1)
        ans = mo + '/' + d + '/' + y
        print(ans)
        break
  except ValueError:
    continue

  file1.close()

#c
