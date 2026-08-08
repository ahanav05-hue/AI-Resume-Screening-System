"""
==========================================================
Resume Parser Module
==========================================================

Supports:

1. PDF Resume Parsing
2. DOCX Resume Parsing
3. Automatic Resume Extraction

==========================================================
"""

import pdfplumber
from docx import Document


# ==========================================================
# PDF PARSER
# ==========================================================

def extract_pdf_text(uploaded_file):

    text = ""

    try:

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

    except Exception as e:

        return f"Error reading PDF: {e}"

    return text


# ==========================================================
# DOCX PARSER
# ==========================================================

def extract_docx_text(uploaded_file):

    text = ""

    try:

        document = Document(uploaded_file)

        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                text += paragraph.text + "\n"

    except Exception as e:

        return f"Error reading DOCX: {e}"

    return text


# ==========================================================
# MAIN RESUME PARSER
# ==========================================================

def extract_resume(uploaded_file):

    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):

        return extract_pdf_text(uploaded_file)

    elif filename.endswith(".docx"):

        return extract_docx_text(uploaded_file)

    else:

        return "Unsupported File Format"


# ==========================================================
# WORD COUNT
# ==========================================================

def word_count(text):

    return len(text.split())


# ==========================================================
# CHARACTER COUNT
# ==========================================================

def character_count(text):

    return len(text)


# ==========================================================
# LINE COUNT
# ==========================================================

def line_count(text):

    return len(text.splitlines())


# ==========================================================
# EMPTY CHECK
# ==========================================================

def is_resume_empty(text):

    return len(text.strip()) == 0