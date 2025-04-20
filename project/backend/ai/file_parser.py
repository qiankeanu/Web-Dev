import fitz
import docx

def extract_text_PDF(file):
    text=""
    pdf=fitz.open(stream=file.read(),filetype='pdf')
    for page in pdf:
        text+=page.get_text()
    return text

def extract_text_from_docx(file):
    doc=docx.Document(file)
    return '\n'.join([p.text for p in doc.paragraphs])