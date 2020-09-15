'''
#Omar_Martinez_1484888
##HW_2.19
'''
#prompt user to enter amount of lemon juice
lemonJuice = float(input('Enter amount of lemon juice (in cups):\n'))
# enetr amount of water
water = float(input('Enter amount of water (in cups):\n'))
#enter amount of nectar and how many servings
agaveNectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
#prints the servings it yields calling on servings as well
print('\nLemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemonJuice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agaveNectar), 'cup(s) agave nectar\n')

NumberofServings = float(input('How many servings would you like to make?\n'))
print('\nLemonade ingredients - yields', '{:.2f}'.format(NumberofServings), 'servings')
serving = NumberofServings / servings

lemonJuice = lemonJuice * serving
water = water * serving
agaveNectar = agaveNectar * serving

print('{:.2f}'.format(lemonJuice),'cup(s) lemon juice')
print('{:.2f}'.format(water),'cup(s) water')
print('{:.2f}'.format(agaveNectar),'cup(s) agave nectar\n')

print('Lemonade ingredients - yields','{:.2f}'.format(NumberofServings),'servings')

lemonGallon = lemonJuice / 16.0
waterGallon = water / 16.0
agaveGallon = agaveNectar / 16.0

print('{:.2f}'.format(lemonGallon), 'gallon(s) lemon juice')
print('{:.2f}'.format(waterGallon),'gallon(s) water')
print('{:.2f}'.format(agaveGallon), 'gallon(s) agave nectar')
