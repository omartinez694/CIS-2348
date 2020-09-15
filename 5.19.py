'''
#Omar_Martinez_1484888
#Hw_5.19
'''
# show the menu to user so user knows what to choose
menu = """Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12"""
print(menu)
#makes a dictionary to define the prices to menu
dict1 = {"Oil change":35,"Tire rotation":19,"Car wash":7,"Car wax":12,"-":"No service"}
#eneter the first and second service
print("\nSelect first service:\n", end="")
service1 = input()
print("Select second service:\n", end="")
service2 = input()
#print invoice
print("\nDavy's auto shop invoice\n")
#if the serice is valid and not - then continue with the input and add the two services and add a monetary value
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