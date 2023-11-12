#сканирование tesseract
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
#точное расположение файла
image = Image.open('')
print(pytesseract.image_to_string(image, lang='rus'))
