import pytesseract
from PIL import Image
import pytesseract as pyt

# Provide tesseract file path as given below

# Check the os and match according to it
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'

# File path of the target image
# image_file = r'E:\Lime Survey\Resource\img_files\(参考)公共図書館における障害者サービスに関する調査研究(H30.8国会図書館)質問紙-07.jpg'
image_file = r'E:\Testing\test_2.jpg'
im = Image.open(image_file)

# Provide Language Options as well
text = pyt.image_to_string(im, 'jpn')
print(text)

