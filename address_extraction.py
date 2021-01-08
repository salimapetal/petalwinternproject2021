string = "DION COPNEY, 216 BRIGHTON AVE, PORTLAND, ME 04101"

name = ""
street = ""
postalCode = string
place = 0
gotName = False

for i in range(len(string)):
    if(not name):
        try:
            int(string[i])
            name = string[:i-1] # -1 to remove the space
            place = i

            gotName = True
        except ValueError:
            pass
    else:
        try:
            int(string[i])
            place += 1
        except ValueError:
            street = string[place+1:] # +1 to remove the space


postalCode = postalCode.replace(name, '')
postalCode = postalCode.replace(street, '')
postalCode = postalCode.replace(' ', '') # removes any unwanted spaces

print ("Name: ", name)
print ("Postal Code: ",postalCode)
print ("Street: ", street)