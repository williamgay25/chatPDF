# main.py

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import json

def main():
    # Load OpenAI API key from environment variable
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Load text chunks from file
    with open('text_chunks.json', 'r') as f:
        texts = json.load(f)

    # Download embeddings from OpenAI and create a vector search index using FAISS
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)

    # Load question answering chain using OpenAI and run it on the user's query
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    while True:
        query = input("Enter your question (type 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        docs = docsearch.similarity_search(query)
        answer = chain.run(input_documents=docs, question=query)
        print("")
        print(answer)
        print("")

if __name__ == "__main__":
    main()