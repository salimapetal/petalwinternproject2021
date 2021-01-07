try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open('/users/salimakazab/desktop/image1.jpg'))  
    return text

print(ocr_core('/users/salimakazab/desktop/image1.jpg'))



