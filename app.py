from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import re
import os
from flask import render_template
import fitz #PyMuPDF


app = Flask(__name__)

###############################################################################
########################### X-Frame-Options for Vulnerabilities ###############
###############################################################################

@app.after_request
def apply_x_frame_options(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response

###############################################################################
########################### Initial Route to start the App ###############
###############################################################################

@app.route('/')
def index():
    return render_template('index.html')


########################################################################
#### This is the Upload  portion of the code ###########################
########################################################################

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf_file' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('pdf_file')
    all_extracted_text = ""

    upload_folder = 'C:\\Users\\jenny\\OneDrive\\Desktop\\Projects\\pdfExport\\app.test\\static\\uploads'
    os.makedirs(upload_folder, exist_ok=True)

    output_folder = 'C:\\Users\\jenny\\OneDrive\\Desktop\\Projects\\pdfExport\\app.test\\static\\extracted_data'
    os.makedirs(output_folder, exist_ok=True)

    for file in files:
        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)

            extracted_text = extract_data(filepath)
            all_extracted_text += extracted_text + "\n\n"

    if all_extracted_text:
        output_filepath = os.path.join(output_folder, 'extracted_text.txt')
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(all_extracted_text)

        # Pass the filename of the extracted text file to the template
        return render_template('extract.html', text=all_extracted_text, filename='extracted_text.txt')

    return redirect(request.url)

########################################################################
#### This is the Extract portion of the code ###########################
########################################################################

def extract_data(filepath):
    # Open the PDF
    doc = fitz.open(filepath)

    # Extract text from each page, only lines 1 to 100
    text = ""
    for page in doc:
        lines = page.get_text().split('\n')
        for line_number, line in enumerate(lines, start=1):
            if 1 <= line_number <= 100:
                text += line + '\n'
    doc.close()
    return text

########################################################################
#### This is the Download of the code ##################################
########################################################################

@app.route('/download')
def download_file():
    filename = request.args.get('filename', 'extracted_text.txt')
    path_to_text_file = f'C:\\Users\\jenny\\OneDrive\\Desktop\\Projects\\pdfExport\\app.test\\static\\extracted_data\\{filename}'
    return send_file(path_to_text_file, as_attachment=True, download_name=filename)

########################################################################
#### This is the Contact portion of the code ###########################
########################################################################

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.config['MAIL_SERVER'] = 'smtp.gmail.com' # your mail server
app.config['MAIL_PORT'] = 123 # your mail server port
app.config['MAIL_USERNAME'] = 'youremail@email.com'
app.config['MAIL_PASSWORD'] = 'mypasswordhere'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    msg = Message("Contact Form Submission", recipients=['recipientemail@email.com'])  # Replace with your recipient email
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)

    flash('Your message has been sent successfully!', 'success')
    return redirect(url_for('contact'))


########################################################################
#### Delete the upload_folers contents #################################
########################################################################


@app.route('/delete-uploads')
def delete_uploads():
    uploads = 'C:\\Users\\jenny\\OneDrive\\Desktop\\Projects\\pdfExport\\app.test\\static\\uploads'
    try:
        shutil.rmtree(uploads)  # This deletes the directory and all its contents
        os.makedirs(uploads, exist_ok=True)  # Recreate the upload_folder after deletion
        return "Uploads successfully deleted."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    



if __name__ == '__main__':
    app.run(debug=True)

 

