'''
print('Birthday Calculator\nCurrent day')
#cmonth,cday, and cyear means current date
cmonth = int(input('Month: '))
cday = int(input('Day: '))
cyear = int(input('Year: '))
#bmonth,bday, and byear means birthdate
print('Birthday')
bmonth = int(input('Month: '))
bday = int(input('Day: '))
byear = int(input('Year: '))
years = byear - cyear - 1
if(bmonth < cmonth):
    years+=1
elif(cmonth==bmonth):
    if(bday<cday):
        years+=1
    if(cmonth==bmonth and cday==bday):
        print('Happy Birthday')
print('You are'+str(years)+'years old.')
'''
###CIS_2348_HW_1.12.1
'''
userNum = int(input())
userNumSquared = userNum * userNum

print(userNumSquared, end='\n')
'''
'''
### HW_1.20

print('Enter integer:')

user_num = int(input())
print('You entered:', user_num)
print(user_num, 'squared is',user_num * user_num)

print('And',user_num, 'cubed is',user_num * user_num * user_num, '!!')

print('Enter another integer:')

user_num2 = int(input())
sum = user_num + user_num2
multi = user_num * user_num2
print(user_num,'+',user_num2,'is' ,sum)
print(user_num,'*',user_num2, 'is', multi)
'''

##HW_2.19
lemonJuice = float(input('Enter amount of lemon juice (in cups):\n'))

water = float(input('Enter amount of water (in cups):\n'))

agaveNectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', servings, 'sevings')
print(lemonJuice, 'cup(s) lemon juice')
print(water, 'cup(s) water')
print(agaveNectar, 'cup(s) agave nectar\n')

desiredNumberOfServings = float(input('How many servings would you like to make?\n'))
print('\nLemonade ingredients - yields', desiredNumberOfServings, 'servings')
serving = desiredNumberOfServings / servings

lemonJuice = lemonJuice * serving
water = water * serving
agaveNectar = agaveNectar * serving

print(lemonJuice,'cup(s) lemon juice')
print(water, 'cup(s) water')
print(agaveNectar,'cup(s) agave nectar\n')

print('Lemonade ingredients - yields',desiredNumberOfServings,'servings\n')

lemonGallon = lemonJuice / 16.00
waterGallon = water / 16.00
agaveGallon = agaveNectar / 16.00

print(lemonGallon, 'gallon(s) lemon juice')
print(waterGallon,'gallon(s) water')
print(agaveGallon, 'gallon(s) agave nectar')

#Hw_3.18 not done yet
'''
wall_height=int(input("Enter wall height (feet): "))

wall_width=int(input("Enter wall width (feet): "))

wall_area=wall_height*wall_width

print("Wall area: "+str(wall_area)+" square feet")

paint_needed=wall_area/350

print("Paint needed: %.6f gallons"%(paint_needed))
'''
'''
#Hw_5.19
menu = """Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12"""
print(menu)
dict1 = {"Oil change":35,"Tire rotation":19,"Car wash":7,"Car wax":12,"-":"No service"}

print("\nSelect first service:\n", end="")
service1 = input()
print("Select second service:\n", end="")
service2 = input()

print("\nDavy's auto shop invoice\n")

if service1!= '-' and service2!='-':
    print("Service 1: "+ service1+", $" + str(dict1[service1]))
    print("Service 2: "+ service2+", $" + str(dict1[service2]))
    Total = dict1[service1]+dict1[service2]
elif service1=='-':
    print("Service 1: " + "No service")
    print("Service 2: " + service2 + ", $" + str(dict1[service2]))
    Total = dict1[service2]
else:
    print("Service 1: " + service1 + ", $" + str(dict1[service1]))
    print("Service 2: " + "No service")
    Total = dict1[service1]

print("\nTotal: $"+str(Total))
'''





