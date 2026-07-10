import streamlit as st
from pypdf import PdfReader

def extract_text_from_pdf(uploaded_file):
    # Initialize the PDF reader
    reader = PdfReader(uploaded_file)
    text = ""
    # Loop through every page and extract text
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text