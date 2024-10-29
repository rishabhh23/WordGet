from PIL import Image
import pytesseract

def extract_text(uploaded_file):
    img = Image.open(uploaded_file)
    extracted_text = pytesseract.image_to_string(img, lang='hin+eng')
    return extracted_text
