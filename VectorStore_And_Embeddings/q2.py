# from langchain.document_loaders import PyPDFLoader
import os
import openai
import sys
import requests
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

def ask_chatgpt(prompt, system_message="", max_tokens=300):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": 0.7,
    }

    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

from langchain_community.document_loaders import PyPDFLoader

loaders = [
    # Duplicate documents on purpose - messy data
    PyPDFLoader(
      "docs/MachineLearning-Lecture01.pdf"),
    PyPDFLoader(
      "docs/MachineLearning-Lecture01.pdf"),
    # PyPDFLoader(
    #   "docs/MachineLearning-Lecture02.pdf"),
    # PyPDFLoader(
    #   "docs/MachineLearning-Lecture03.pdf")
]
docs = []
for loader in loaders:
    docs.extend(loader.load())

#################################################################################################

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap = 150
)

splits = text_splitter.split_documents(docs)

print("*****************************************************")

print(len(splits))

print("*****************************************************")

#################################################################################################

from langchain_community.embeddings import OpenAIEmbeddings

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

sentence1 = "i like dogs"
sentence2 = "i like canines"
sentence3 = "the weather is ugly outside"

embedding1 = embedding.embed_query(sentence1)
embedding2 = embedding.embed_query(sentence2)
embedding3 = embedding.embed_query(sentence3)

import numpy as np

print("*****************************************************")

print(np.dot(embedding1, embedding2))
print(np.dot(embedding1, embedding3))
print(np.dot(embedding2, embedding3))

print("*****************************************************")

#################################################################################################

persist_directory = 'docs/chroma/'

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

vectordb = Chroma.from_documents(
    documents=splits,
    embedding=embedding,
    persist_directory=persist_directory
)

all_docs = vectordb.get()

print("*****************************************************")

print(len(all_docs))

print("*****************************************************")

#################################################################################################

question = "is there an email I can ask for help"
docs = vectordb.similarity_search(question, k=3)

num_docs = len(docs)

print("*****************************************************")

print(num_docs)

first_doc_content = docs[0].page_content
print(first_doc_content)

print("*****************************************************")

#################################################################################################

question = "what did they say about matlab?"

docs = vectordb.similarity_search(question,k=5)

print("*****************************************************")

print(docs[0])

print(docs[1])

print("*****************************************************")

#################################################################################################

question = "what did they say about regression in the third lecture?"

docs = vectordb.similarity_search(question,k=5)

print("************************")

for doc in docs:
    print(doc.metadata)

print(docs[4].page_content)

print("*****************************************************")

#################################################################################################