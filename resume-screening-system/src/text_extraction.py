import pdfplumber
from docx import Document

def extract_text(uploaded_file):
    """
    Extract text from a Streamlit UploadedFile (PDF or DOCX).
    """
    text = ""
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif filename.endswith(".docx"):
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

    return text.strip()

