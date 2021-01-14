import imagetotext
import re

a_string = imagetotext.ocr_core()
#rint(type(a_string))
#lastname = input('Enter last name: ')
lastname = "zheng"
#zipcode = input("Enter zipcode")
zipcode = "27617"
matches = re.finditer(lastname, a_string)
matches_positions = [match.start() for match in matches]
print(matches_positions)