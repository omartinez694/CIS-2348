#Martinez_Omar_psid#1484888


l = input()

l = l.split(" ")
o = {}

for each in l:
    if each in o:
        o[each] = o[each] + 1
    else:
        o[each] = 1

for each in l:
    print(each, o[each])
