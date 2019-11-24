try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def image_to_text(filename):
    """
    This function will handle the core OCR processing of images
    """
    text = pytesseract.image_to_string(Image.open(filename))  # it use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
