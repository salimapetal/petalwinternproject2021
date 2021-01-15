

string = 

name = ""
street = string
postalCode = ""
place = 0
gotName = False

for i in range(len(string)):
    if(not name):
        try:
            int(string[i])
            name = string[:i-1] 
            place = i

            gotName = True
        except ValueError:
            pass
    else:
        try:
            int(string[i])
            place += 1
        except ValueError:
            street = string[place+1:] 

postalCode = postalCode.replace(name, '')
postalCode = postalCode.replace(street, '')
postalCode = postalCode.replace(' ', '') 

print ("Name: ", name)
print ("Postal Code: ",postalCode)
print ("Street: ", street)

#address should be "DION COPNEY, 216 BRIGHTON AVE, PORTLAND, ME 04101"