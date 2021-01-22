# Petal Winternship Project 2021

## "imagetotext.py" Module - Code to extract text from images

This module uses the ocr_core() function to extract text from an image. The image should have its file path written in the function.
The extracted text is then returned. The module then uses the extract_text_from_image() function to return the extracted text. 
This function is referenced in the next module SplitUtilityBill.py.  
#### Libraries Installed: 
     -Google Tesseract OCR
	 -Python Imaging Library (PIL)
#### How to install each library:
	 -Google Tesseract OCR: brew install tesseract 
     -Python Imaging Library (PIL): sudo pip3 install pil 
     -or you can install the “friendly” PIL fork: pip3 install Pillow

## SplitUtilityBill.py module - Code to split utility bill 
This module passes the filename into the function split_utility_bill. Then the extract_text_from_image() function is imported and returns the extracted text. 
Regex is then used to clean the string. The string is split by whitespace and returns a list. The function is then referenced in addresscode.py. 
#### Libraries installed:
     -Regex (Regular Expressions) 
     -How to install library: $ pip3 install regex

## Iteration.py module 
This module will create a universal path that recognizes what is uploaded in the server, without specific filename (it works with different images)
We are calling this module iteration.py module. We are then going to import this module into imagetotext.py (where text is extracted from image). 

## Addresscode.py module
In the module "addresscode.py" “addresscode.py”,
we aim to extract the code from the image, in which the text has already been extracted and split word by word. 
The logic of this code, works for utility bills in which the address is contained between the last name and the Zip Code, so it recognizes where these two pieces of information are and extracts the address including the Zip Code. 
The output should be an address in the correct format such as, Address is: 380 Broadway Avenue NY 11456

## Live Server
Set up live server: There is an extension on Visual Studio Code
To upload files you’re also going to need Flask, a micro web framework written in Python. 

## App.py module 
This module is a Flask application that builds the web application. In app.py functions are binded to the URLs /, /success, and /upload. 
The first route returns the HTML template that includes the visuals for the web page. The second route returns a success page after the address has been extracted from the uploaded image file. The third route takes the user input (first name, last name, zip code, and uploaded file) from the web page and saves it to a configured folder named UPLOAD_FOLDER. After the address is extracted the user is redirected to the success page which returns the extracted info. 
#### Libraries installed:
     -Flask
     -How to install library
     -pip3 install Flask

