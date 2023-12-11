from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import re
import os
from flask import render_template
import fitz #PyMuPDF


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

"""
@app.route('/')
def index():
    # This pulls up an HTML form for uploading the PDJ files. 
    return '''
    <form method="post" action="/upload" enctype="multipart/form-data">
      <input type="file" name="pdf_file">
      <input type="submit" value="Upload">
    </form>'''
"""
    
#################################################################################
## Route to handle the file upload and trigger the extraction process#############
################################################################################

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf_file' not in request.files:
        return 'No file part'
    file = request.files['pdf_file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        upload_folder = 'C:\\Users\\jenny\\OneDrive\\Desktop\\Projects\\pdfExport\\app.test\\static\\uploads'  # Update this path
        os.makedirs(upload_folder, exist_ok=True)  # Create the directory if it doesn't exist
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        extract_data(filepath)  # Function to extract data
        return '<a href="/download">Download Text File</a>'

def extract_data(filepath):
    import fitz  # PyMuPDF

    # Open the PDF
    doc = fitz.open(filepath)

    # Extract text from each page
    text = ""
    for page in doc:
        text += page.get_text()

        # Extract annotations (comments)
        annotations = page.annots()
        if annotations:
            for annot in annotations:
                if annot.type[0] == 8:  # Text annotations
                    text += "Comment: " + annot.info["content"] + "\n"

    # Output file path (adjust as needed)
    output_path = r"C:\Users\jenny\OneDrive\Desktop\Projects\pdfExport\app.test\static\extracted_data.txt"
    
    # Write the extracted text to a file
    with open(output_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)
        

    # Close the PDF document
    doc.close()


    
@app.route('/download')
def download_file():
    path_to_text_file = r"C:\Users\jenny\OneDrive\Desktop\Projects\pdfExport\app.test\static\extracted_data.txt"
    return send_file(path_to_text_file, as_attachment=True)
    


if __name__ == '__main__':
    app.run(debug=True)




#
#def extract_data(filepath):
#    reader = PdfReader(filepath)
#    text = reader.pages[0].extract_text()
    
#    print(text)

    # Function to safely get group data
#    def safe_search(pattern, text):
#        match = re.search(pattern, text)
#        return match.group(1) if match else None

    # Regular expression patterns
    #agency_number_pattern = r"Agency Number:\s*(\d+)"
#    agency_number_pattern = r"1\.\s*Agency number\s*(\d+)"

#    agency_name_pattern = r"Agency Name:\s*(.+)"
#    date_pattern = r"Date:\s*(\d{2}/\d{2}/\d{4})"
#    batch_date_pattern = r"Batch Date:\s*(\d{2}/\d{2}/\d{4})"
#    batch_type_pattern = r"Batch Type:\s*([A-Za-z0-9]+)"
#    batch_no_pattern = r"Batch No.:\s*(\d+)"
#    seq_no_pattern = r"Seq. No.:\s*(\d+)"
#    documentno_SFXNo_pattern = r"Document no./SFX No.:\s*([\w/]+)"
#    amount_pattern = r"Amount:\s*\$?(\d+\.\d{2})"
 #   reason_code_pattern = r"Reason Code:\s*([A-Za-z0-9]+)"
#    print(text)

    # Extracting data using the safe_search function
#    agency_number = safe_search(agency_number_pattern, text)
#    agency_name = safe_search(agency_name_pattern, text)
#    date = safe_search(date_pattern, text)
#    batch_date = safe_search(batch_date_pattern, text)
#    batch_type = safe_search(batch_type_pattern, text)
#    batch_no = safe_search(batch_no_pattern, text)
#    seq_no = safe_search(seq_no_pattern, text)
#    documentno_SFXNo = safe_search(documentno_SFXNo_pattern, text)
#    amount = safe_search(amount_pattern, text)
#    reason_code = safe_search(reason_code_pattern, text)
    
#    print(agency_number,agency_name,date,batch_date,batch_type,batch_no,seq_no,documentno_SFXNo,amount,reason_code)

    # Save the extracted information to a text file
    #with open("/path/to/extracted_data.txt", "w") as file:
#    with open(r"C:\Users\jenny\OneDrive\Desktop\Projects\pdfExport\app.test\static\extracted_data.txt", "w") as file:
#        file.write(f"Agency Number: {agency_number}\n")
#        file.write(f"Agency Name: {agency_name}\n")
#        file.write(f"Date: {date}\n")
#        file.write(f"Batch Date: {batch_date}\n")
#        file.write(f"Batch Type: {batch_type}\n")
#        file.write(f"Batch No: {batch_no}\n")
#        file.write(f"Seq No: {seq_no}\n")
#        file.write(f"Document No: {documentno_SFXNo}\n")
#        file.write(f"Amount: {amount}\n")
#        file.write(f"Reason Code: {reason_code}\n")'''
 

