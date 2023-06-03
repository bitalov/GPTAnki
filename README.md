# GPTAnki

GPTAnki is a simple web application that uses OpenAI's GPT-3.5 or GPT-4 to generate Anki flashcards from a given PDF file. The application uses Streamlit for the frontend and PyPDF2 for PDF text extraction.

## Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
- [Deployment](#deployment)
- [Try it Online](#try-it-online)

## Requirements

To set up the environment for GPTAnki, you'll need to install the required Python libraries. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain the following:

```
streamlit
PyPDF2
openai
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/username/GPTAnki.git
```

2. Navigate to the project directory:

```bash
cd GPTAnki
```

3. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

The application should now be running on your local machine at `http://localhost:8501/`.

## Deployment

To deploy the application, you can use a platform like [Render](https://render.com/). Follow these steps:

1. Create an account on [Render](https://render.com/) and sign in.
2. Click on the "New" button in the dashboard and choose "Web Service".
3. Connect your GitHub account and select the GPTAnki repository.
4. In the "Environment" section, choose "Python" and set the "Build command" to:

```bash
pip install -r requirements.txt
```

5. Set the "Start command" to:

```bash
streamlit run AnkiGPT.py
```

6. Click on the "Create Web Service" button to deploy the application.

The application should now be deployed and accessible via the provided URL.

## Try it Online

You can try the GPTAnki application online by visiting the following link:

[https://gptanki.onrender.com/](https://gptanki.onrender.com/)
