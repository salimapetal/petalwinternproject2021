try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open('/Users/salimakazab/Desktop/petalwinternproject21/petalwinternproject2021/files/utilitybill1.jpg'))  #image to text works
    return text

print(ocr_core('/Users/salimakazab/Desktop/petalwinternproject21/petalwinternproject2021/files/utilitybill1.jpg'))

#f = open("text.txt", "w")
#f.write(ocr_core('/Users/salimakazab/Desktop/petalwinternproject21/petalwinternproject2021/files/utilitybill1.jpg'))
#f.close()