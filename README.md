# LangChain

# Flask Chatbot with LangChain & OpenAI

This project demonstrates how to build a conversational AI chatbot using Flask, LangChain, and OpenAI's GPT-3.5, which answers user queries based on the content of a PDF document.

## Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Technology Stack](#technology-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Routes](#routes)
7. [Contributing](#contributing)
8. [License](#license)

## Overview

The chatbot uses LangChain for document processing and OpenAI GPT-3.5 for natural language understanding. Users can upload PDF documents, which are processed and indexed, allowing the chatbot to answer questions based on the document content. This project demonstrates the power of combining AI models with document-based search.

## Key Features

- **PDF Document Upload**: Upload PDF files for document processing.
- **Text Splitting**: Large documents are split into chunks for efficient handling.
- **Conversational AI**: Uses OpenAI GPT-3.5 to respond to user queries based on the document content.
- **Chat History**: Maintains chat history for contextual responses.

## Technology Stack

- **Flask**: Python-based web framework to handle user requests and serve the application.
- **LangChain**: A framework for building applications with LLMs (Large Language Models), used for document loading, splitting, and retrieval-based question answering.
- **OpenAI GPT-3.5**: Language model for generating responses based on document context.
- **PyPDFLoader**: A tool for loading and extracting text from PDF files.
- **DocArrayInMemorySearch**: Stores and retrieves document embeddings.
- **dotenv**: Loads environment variables, such as the OpenAI API key.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/flask-chatbot-langchain-openai.git
   cd flask-chatbot-langchain-openai

2. **Install dependencies**:

Make sure you have Python 3.7+ installed. Then, create a virtual environment and install the required packages.

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Set up environment variables:

3. **Create a .env file in the project root directory and add your OpenAI API key:**

bash
Copy code
OPENAI_API_KEY=your-openai-api-key


Usage
4. **Start the Flask server:**

bash
Copy code
python app.py
Interact with the chatbot:

Go to http://localhost:5006 in your web browser.
Upload a PDF document to enable the chatbot to process the file.
Ask questions related to the document, and the chatbot will respond based on the content.

Routes
/: The main page where users can upload a PDF and interact with the chatbot.
/load_db (POST): Uploads a PDF document for processing. The document is saved and indexed for retrieval.
/chat (POST): Sends a user query to the chatbot. The chatbot responds based on the document content.
/clear_history (POST): Clears the chat history for a fresh start.

Contributing
Feel free to fork this repository, submit issues, and make pull requests. Contributions are welcome!
