import imagetotext
import re
a_string = imagetotext.ocr_core()
lastname = input ('Zheng')

zipcode = input ('27617')
matches = re.finditer(lastname, zipcode, a_string)

matches_positions = [match.start() for match in matches]
print(matches_positions)

