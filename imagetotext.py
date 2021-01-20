try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def extract_text_from_image(filename):
    return ocr_core(filename)

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(f'/Users/salimakazab/Desktop/petalwinternproject2021/uploads/{filename}'))  #opens filename following the uploaded image
    return text

if __name__ == "__main__" :
    print(ocr_core())