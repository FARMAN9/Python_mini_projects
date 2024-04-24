import pytesseract
from PIL import Image
import os 

def main():
    # Specify the path to the image file
    image_path = os.path.abspath('images.jpg')

    if not os.path.exists(image_path):
        print(f"File '{image_path}' does not exist. Please check the file path.")
    else:
       print(f"File '{image_path}' found.")
    
    # Specify the path to the Tesseract OCR executable
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    
    # Open the image file
    img = Image.open(image_path)
    
    # Perform OCR using pytesseract
    # Specify the language as 'eng' (English) or another language as needed
    text = pytesseract.image_to_string(img, lang='eng')
    
    # Print the extracted text
    print("Extracted text from the image:")
    print(text)

if __name__ == '__main__':
    main()
