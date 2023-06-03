import streamlit as st
import PyPDF2
import openai
import os
import base64

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    extracted_text = " ".join([page.extract_text() for page in pdf_reader.pages])
    return extracted_text

def split_text_into_chunks(text, chunk_size):
    chunks = []
    start = 0
    end = chunk_size
    while start < len(text):
        chunk = text[start:end]
        chunks.append(chunk)
        start = end
        end += chunk_size
    return chunks

def generate_anki_flashcards(text, chunk_size, api_key, model_choice):
    openai.api_key = api_key
    text_chunks = split_text_into_chunks(text, chunk_size)
    flashcards = ''
    for i, chunk in enumerate(text_chunks):
        message_prompt = [
                {"role": "system", "content": "You are a helpful assistant and specialist in creating flashcards."},
                {"role": "user", "content": f"Create Anki flashcards with the provided text using a format: question;answer. Keep the question and the corresponding answer on the same line {chunk}"}
                ]

        api_response = openai.ChatCompletion.create(
            model=model_choice,
            messages=message_prompt,
            temperature=0.2,
            max_tokens=2048
        )

        flashcards += api_response['choices'][0]['message']['content']

        if i == 0:
            break

    return flashcards

def get_file_download_link(text_file, filename):
    b64 = base64.b64encode(text_file.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}">Download Flashcards</a>'

st.title('Anki Flashcard Generator')

uploaded_file = st.file_uploader('Please upload your PDF file', type='pdf')

chunk_size = st.number_input('Enter the chunk size (default is 1000)', min_value=1, value=1000, step=1)

api_key = st.text_input('Please enter your OpenAI API Key')
model_choice = st.selectbox('Select the AI model to be used', ['gpt-3.5-turbo', 'gpt-4'])

if api_key.strip() == '':
    st.error('Please input your OpenAI API key before proceeding.')
elif uploaded_file is None:
    st.error('Please upload a PDF file before proceeding.')
elif st.button('Generate Flashcards'):
    pdf_text = extract_text_from_pdf(uploaded_file)
    flashcards = generate_anki_flashcards(pdf_text, chunk_size, api_key, model_choice)
    st.success('Flashcards successfully created! Click the link below to download.')
    download_link = get_file_download_link(flashcards, 'flashcards.txt')
    st.markdown(download_link, unsafe_allow_html=True)
