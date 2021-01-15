from imagetotext import extraction
import re

ext = extraction

#clean string
pat = re.compile(r'[^0-9a-zA-Z ]+')
ext = re.sub(re.compile (r'\n'), ' ', ext)
ext = re.sub(pat, '', ext).lower()

#split string
splitdoc = ext.split()

#for loop to iterate over words array
#for split in splits:
	#splitdoc=print(split)
print (extraction)
