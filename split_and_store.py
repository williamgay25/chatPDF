# split_and_store.py

import os
import json
from PyPDF2 import PdfReader

def custom_text_splitter(text, chunk_size=256, chunk_overlap=64):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        if end == len(text):
            break
        start = end - chunk_overlap
    return chunks

def main():
    # Read PDF file and extract text
    try:
        with open('./4034-Exam2-Notes.pdf', 'rb') as file:
            reader = PdfReader(file)
            raw_text = ''
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    raw_text += text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return

    # Split text into smaller chunks
    texts = custom_text_splitter(raw_text)

    # Store chunks in a file
    with open('text_chunks.json', 'w') as f:
        json.dump(texts, f)

if __name__ == "__main__":
    main()
