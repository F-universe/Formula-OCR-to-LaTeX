from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from formula_ocr import extract_latex

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    latex_output = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No image uploaded.'
        image = request.files['image']
        if image.filename == '':
            return 'No selected file.'
        if image:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename))
            image.save(filepath)
            latex_output = extract_latex(filepath)
    return render_template('index.html', latex_output=latex_output)

if __name__ == '__main__':
    app.run(debug=True)
