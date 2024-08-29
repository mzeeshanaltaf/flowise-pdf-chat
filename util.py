import streamlit as st
import requests
import tempfile
import os


def get_file_path(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name
        filename, _ = os.path.splitext(uploaded_file.name)
        return temp_pdf_path, filename


def create_vectordb(uploaded_file):
    API_URL = "http://localhost:3000/api/v1/vector/upsert/2667672d-a65e-48e8-87cf-c868b43a95a2"

    file_path, file_name = get_file_path(uploaded_file)

    form_data = {
        "files": (file_path, open(file_path, 'rb'))
    }
    body_data = {
        "stripNewLines": True,
    }
    with st.spinner('Creating Vector DB ...'):
        _ = requests.post(API_URL, files=form_data, data=body_data)
        st.success('Vector DB has been created successfully!')


def get_llm_response(question):
    API_URL = "http://localhost:3000/api/v1/prediction/2667672d-a65e-48e8-87cf-c868b43a95a2"
    payload = {
        "question": question,
    }
    response = requests.post(API_URL, json=payload)
    output = response.json()
    return output['text']
