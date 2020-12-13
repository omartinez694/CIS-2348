#Omar_Martinez_1484888
import csv
import pprint
import datetime
from operator import itemgetter
#structures my objects
pp = pprint.PrettyPrinter(indent=4)

date = []
price = []
items = dict()
listoutput = []

# open first csv and read it
manufacturer_list = list()

with open('ManufacturerList.csv', 'r') as f:
    content = csv.reader(f, delimiter=',')
    for row in content:
        manufacturer_list.append(row)

# open second csv and read it while inserting into the locations i need them to be
price_list = list()
with open('PriceList.csv', 'r') as c:
    content = csv.reader(c, delimiter=',')
    for row in content:
        price_list.append(row)

# open third csv and read it while inserting them into the columns i need them to be in
service_date_list = list()
with open('ServiceDatesList.csv', 'r') as c:
    content = csv.reader(c, delimiter=',')
    for row in content:
        service_date_list.append(row)

# Create a dictionary here
full_inventory_dict = dict()



for id, brand, type, ifdamged in manufacturer_list:
    full_inventory_dict[id] = [brand, type, ifdamged]

pp.pprint(full_inventory_dict)
#appending the list
for id, price in price_list:
    full_inventory_dict[id].append(price)

pp.pprint(full_inventory_dict)

# append service date
for id, service in service_date_list:
    full_inventory_dict[id].append(service)
print()

print()
print("Full Inventory")
print("------------------")
pp.pprint(full_inventory_dict)

output = []
for id, fields in full_inventory_dict.items():
    row = [id]
    row.extend(fields)
    output.append(row)
#arranging the list
arranged_output = []
for id, brand, type, ifdamged, price, service in output:
    arranged_output.append([id, brand, type, price, service, ifdamged])

output = arranged_output

output = sorted(output, key=itemgetter(1, 2))  # 2nd and 3rd column


print()
print("List of Lists to store into CSV:")
print("------------------")
pp.pprint(output)

with open('FullInventory.csv', 'w', newline='') as f:
    thewriter = csv.writer(f, delimiter=',')
    for row in output:
        thewriter.writerow(row)

print()
#writing laptop inventory
print("Now write to LaptopInventory.csv")
print("------------------")
pp.pprint(output)
#laptopt inventory as a list
laptop_inv_output = []
for id, brand, item_type, price, service, ifdamged in output:
    #if the item type is comparing to laptop then show laptop
    if item_type == "laptop":
        #set them in a orderbut without the item type
        laptop_inv_output.append([id, brand, price, service, ifdamged])

laptop_inv_output = sorted(laptop_inv_output, key=itemgetter(0))

pp.pprint(laptop_inv_output)

with open('LaptopInventory.csv', 'w', newline='') as f:
    thewriter = csv.writer(f, delimiter=',')
    for row in laptop_inv_output:
        print(row)
        thewriter.writerow(row)

print()
print("PastServiceDateInventory.csv")
print("------------------")

past_service_date_inv = []
for id, brand, item_type, price, service, ifdamged in output:
    #setting aprt from service dates as well distingushing from current date
    service_date = datetime.datetime.strptime(service, '%m/%d/%Y')
    now = datetime.datetime.now()
    if service_date < now:
        past_service_date_inv.append([id, brand, item_type, price, service, service_date])
past_service_date_inv = sorted(past_service_date_inv, key=itemgetter(5))

with open('PastServiceDateInventory.csv', 'w', newline='') as f:
    thewriter = csv.writer(f, delimiter=',')
    for row in past_service_date_inv:
        thewriter.writerow([row[0], row[1], row[2], row[3], row[4]])

pp.pprint(past_service_date_inv)

print()
print("DamagedInventory.csv")
print("------------------")
damaged_inv_output = []
#open up
for id, brand, item_type, price, service, ifdamged in output:
    #equal to damged then show it
    if ifdamged == "damaged":
        #the way to show it
        damaged_inv_output.append([id, brand, item_type, price, service])
pp.pprint(damaged_inv_output)
damaged_inv_output = sorted(damaged_inv_output, key=itemgetter(3))

with open('DamagedInventory.csv', 'w', newline='') as f:
    thewriter = csv.writer(f, delimiter=',')
    for row in damaged_inv_output:
        thewriter.writerow(row)

#2 interactive Inventory Query Capability

manufacturerName = input("Enter manufacturers's name:\n")
itemType = input("Enter item's type:\n")

itemmz = ""
itemz = []
typee = ""
for id, brand, item_type, price, service, ifdamged in output:
    if manufacturerName == brand:
        itemmz = brand

    if itemType == item_type:
        typee = item_type
    itemmz.append([id, brand, price])
if (itemz == "" or typee == ""):
    print("No such item in inventory")

print(itemz)
