Formula OCR to LaTeX is a web application developed using Python
and Flask that allows a user to upload an image or screenshot of a 
mathematical formula and receive its corresponding LaTeX code as output. 
The system uses Tesseract OCR to extract text from the image and performs
basic transformations to approximate the output into proper LaTeX format. 
It is designed to help students, researchers, or anyone working with mathematical
documents convert visual formulas into editable LaTeX code efficiently. The user 
interface is simple: the user selects an image from their computer, submits the form,
and the recognized LaTeX code is displayed. The backend loads the image using Pillow, 
processes it with Tesseract, and then applies pattern replacements such as replacing 
square roots with \sqrt, slashes with \frac, and common symbols like pi, alpha, beta,
and theta with their LaTeX equivalents. The application works locally and requires 
Tesseract-OCR to be installed and accessible from the system’s path. It supports common 
formats like PNG and JPG and provides a lightweight solution without needing heavy
models or GPU acceleration. It is especially useful when formulas are found in
scanned books, notes, or screenshots where typing LaTeX manually would be time-consuming.
The project is modular and extendable, allowing users to improve the pattern recognition
or integrate MathJax for rendered preview of the LaTeX result. The goal of this tool is
to speed up mathematical document preparation and offer a practical example of combining OCR
technology with a web-based interface.
