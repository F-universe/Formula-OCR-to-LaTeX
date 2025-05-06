import pytesseract
from PIL import Image

# Make sure Tesseract is correctly installed and in PATH
# Example for Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extract_latex(image_path):
    img = Image.open(image_path)
    raw_text = pytesseract.image_to_string(img, config='--psm 6')
    latex = post_process(raw_text)
    return latex

def post_process(text):
    replacements = {
        '^': r'^',
        '/': r'\\frac',
        '=': '=',
        'sqrt': r'\\sqrt',
        'pi': r'\\pi',
        'theta': r'\\theta',
        'alpha': r'\\alpha',
        'beta': r'\\beta',
    }
    for key, val in replacements.items():
        text = text.replace(key, val)
    return text.strip()
