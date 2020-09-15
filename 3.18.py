'''
#Omar_Martinez_1484888
#Hw_3.18
'''
#enter the height of and width of wall
height = float(input('Enter wall height (feet):\n'))
width = float(input('Enter wall width (feet):\n'))
#calculates the area and divided by the 250 square ft and tells you the amount of cans needed
area = round(height * width)
paint_needed = area / 350
cans = round(paint_needed)
#print the wall area and decide paint needed
print('Wall area: ' + str(area) + ' square feet')
print('Paint needed: %.2f gallons' % paint_needed)
print('Cans needed: ' + str(cans) + ' can(s)')

#prices decided by what color user enters
color = input('\nChoose a color to paint the wall:\n')
if color == 'red':
    cost = 35 * cans
elif color == 'blue':
    cost = 25 * cans
elif color == 'green':
    cost = 23 * cans
else:
    cost = 0
print('Cost of purchasing',color,'paint: $' + str(cost))
