txt= import imagetotext

mylist = txt.split ('/n')
r = re.compile(r"(\d{1,10}(\w+){1,10}( (\w+){1,10})?(\w+){1,10}[,.]((\w+){1,10}(,)? [A-Z]{2}( [0-9]{5})?)?)")
newlist = list(filter(r.match, mylist)) # Read Note
print(newlist)