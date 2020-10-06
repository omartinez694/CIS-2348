password = input()
newpass = ""

for c in password:
   if c == 'i':
       newpass = newpass + '!'
   elif c == 'a':
       newpass = newpass + '@'
   elif c == 'm':
       newpass = newpass + 'M'
   elif c == 'B':
       newpass = newpass + '8'
   elif c == 'o':
       newpass = newpass + '.'
   else:
       newpass = newpass + c
newpass = newpass + "q*s"
print(newpass)