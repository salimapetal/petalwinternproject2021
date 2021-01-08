
import os
import ocrmypdf
import requests
import pdfplumber

invoice_pdf = '/Users/miahkirton/Documents/test6.pdf'
 
with pdfplumber.open(invoice_pdf) as pdf: 
    page = pdf.pages[0]
    text = page.extract_text()
    print(text)
    #print(type(text))
     
if text == None :
    os.system(f'ocrmypdf {invoice_pdf} output.pdf') 

    with pdfplumber.open('output.pdf') as pdf:
        page = pdf.pages[0]
        text = page.extract_text(x_tolerance=2)
        print(text)
else: 
    print(text)

lines = text.split('/n') 
import re
street_address = re.search(r'\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)', text)
print(street_address)