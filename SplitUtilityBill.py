from imagetotext import extract_text_from_image
import re
#clean string
#for loop to iterate over words array
#for split in splits:
	#splitdoc=print(split)
def split_utility_bill(filename):
	ext = extract_text_from_image(filename)
	print(ext)
	pat = re.compile(r'[^0-9a-zA-Z ]+')
	ext = re.sub(re.compile (r'\n'), ' ', ext)
	ext = re.sub(pat, '', ext).lower()
	#split string
	splitdoc = ext.split()
	print(splitdoc)
	return splitdoc