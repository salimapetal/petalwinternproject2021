import imagetotext
import re

str= imagetotext.ocr_core()

#clean string
pat = re.compile(r'[^0-9a-zA-Z ]+')
str = re.sub(pat, '', str).lower()

#split string
splits = str.split()

#for loop to iterate over words array
for split in splits:
	print(split)