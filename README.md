# PDF Data Extraction Tool

This tool is designed to efficiently extract text and annotations from PDF files, providing a simple yet powerful solution for handling PDF data. It leverages the capabilities of PyMuPDF, a versatile library that makes PDF parsing seamless and effective.

## Features

- **Text Extraction**: Extracts all readable text from each page of the PDF.
- **Annotation Extraction**: Retrieves text annotations, adding an extra layer of data retrieval.
- **Ease of Use**: Simplified usage with a straightforward function call.
- **Output Customization**: Saves extracted data in a text file, easily customizable to suit various project needs.

## Installation

Before using this tool, ensure that you have PyMuPDF installed in your Python environment:

```bash
1. Make sure you have Python >= 3.10 on your machine.
2. Create a virtual environment
  python -m venv venv
3. Activate the virtual environment
  .\venv\Scripts\activate.ps1
4. Upgrade pip
  pip install --upgrade pip
5. Install project dependencies
  pip install -r requirements.txt
6. Run the app
  set FLASK_DEBUG=1
  python app.py

## Usage

The `extract_data` function is the core of this tool. Simply pass the file path of your PDF, and the function will handle the rest.

```python
from extract_data import extract_data

# Path to your PDF file
pdf_file_path = 'path/to/your/pdf/file.pdf'

# Extract data from the PDF
extract_data(pdf_file_path)

# The function will create a text file containing all extracted text and annotations.

```
## Contributing
Contributions to this project are welcome! Whether it's improving the extraction algorithm, adding new features, or fixing bugs, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
If you have any questions or suggestions, please feel free to contact me.

### Thank you for using or contributing to this PDF data extraction tool!


