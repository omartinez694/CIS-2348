'''
#Omar_Martinez_1484888
#Hw_project_1
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

