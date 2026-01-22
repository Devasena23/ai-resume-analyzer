import streamlit as st
import pdfplumber
import docx
from llm import analyze_resume

# Extract PDF text
def extract_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Extract DOCX text
def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

st.title("AI Resume Analyzer with Open Source LLM")

file = st.file_uploader("Upload Resume", type=["pdf","docx"])

if file:
    if file.name.endswith(".pdf"):
        resume_text = extract_pdf(file)
    else:
        resume_text = extract_docx(file)

    st.subheader("Resume Text")
    st.text_area("", resume_text, height=300)

    if st.button("Analyze Resume with AI"):
        with st.spinner("AI is analyzing..."):
            result = analyze_resume(resume_text)
        st.subheader("AI Feedback")
        st.write(result)
