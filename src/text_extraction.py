import pdfplumber
import docx
import os

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file."""
    text = ""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        raise ValueError(f"Error extracting PDF: {e}")
    return text

def extract_text_from_docx(uploaded_file):
    """Extract text from a DOCX file."""
    text = ""
    try:
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        raise ValueError(f"Error extracting DOCX: {e}")
    return text

def extract_text(uploaded_file):
    """Extract text from a resume file (PDF or DOCX)."""
    ext = os.path.splitext(uploaded_file.name)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(uploaded_file)
    elif ext == '.docx':
        return extract_text_from_docx(uploaded_file)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
