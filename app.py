import os
from addresscode import extract_address
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
app=Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/') #@app.route('/', methods=['POST']) could not be done error : method not allowed
def upload_form():
    return render_template('index.html')
@app.route('/success')
def success():
    return ('<!DOCTYPE html><html><h1>http://127.0.0.1:7000/success</h1></html>')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        payload = request.form.to_dict()
        fname = payload['fname'].lower()
        lname = payload['lname'].lower()
        zipcode = payload['zipcode']
        print(payload)
        file = request.files['file']
        first_name = request.form.get("fname")
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            output_address = extract_address(filename = filename,last_name=lname, zip_code=zipcode)
            flash('File successfully uploaded')
            return jsonify({'address': output_address})
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
if __name__ == "__main__":
    app.run(host = '127.0.0.1',port = 7000, debug = False)