import os
import openai
import requests
import sys
from dotenv import load_dotenv, find_dotenv
import os
os.environ["FFMPEG_BIN"] = r"C:\Users\ranis\Downloads\ffmpeg-2024-10-31-git-87068b9600-full_build\ffmpeg-2024-10-31-git-87068b9600-full_build\bin\ffmpeg.exe"  # Replace this path with the actual path to ffmpeg.exe

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

# from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(r"https://see.stanford.edu/materials/aimlcs229/transcripts/MachineLearning-Lecture01.pdf")
pages = loader.load()

len(pages)

page = pages[0]

print("*****************************************************")

print(page.page_content[0:500])

print("*****************************************************")

page.metadata

#####################################################################################################################

import yt_dlp
ffmpeg_path = r"C:\Users\ranis\Downloads\ffmpeg-2024-10-31-git-87068b9600-full_build\ffmpeg-2024-10-31-git-87068b9600-full_build\bin\ffmpeg.exe"  # Replace this path with the actual path to ffmpeg.exe

url = "https://www.youtube.com/watch?v=jGwO_UgTS7I"

ydl_opts = {
    'format': 'best',
    'ffmpeg_location': ffmpeg_path,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}

print("*****************************************************")
print("Downloading Link")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("*****************************************************")

#######################################################################################################################

from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://github.com/basecamp/handbook/blob/master/37signals-is-you.md")

docs = loader.load()

print("*****************************************************")

print(docs[0].page_content[:500])

print("*****************************************************")

#######################################################################################################################

