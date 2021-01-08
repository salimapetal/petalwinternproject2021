import re
text = "Hello, my name is . I live in 329 Yellow Street, Syracuse NY 11346. I have two cats."
first_half, second_half = text[:len(text)//2], text[len(text)//2:]
regexp = "(\d{1,10}( \w+){1,10}( ( \w+){1,10})?( \w+){1,10}[,.](( \w+){1,10}(,)? [A-Z]{2}( [0-9]{5})?)?)"
print(first_half)
print(second_half)
address = re.findall(regexp, first_half)
address2 = re.findall(regexp, second_half)
print(address)
print(address2)