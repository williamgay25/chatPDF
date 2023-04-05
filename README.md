# chatPDF

This repository contains a simple chatbot that answers questions based on the contents of a provided PDF file. The chatbot first processes the PDF, splitting its text into smaller chunks, and then uses OpenAI's language model to generate relevant answers to user queries.

## Prerequisites

- Python 3.7 or newer
- A PDF file to use as the source of information for the chatbot
- OpenAI API key

## Getting Started

1. Clone the repository:
```shell
git clone git@github.com:williamgay25/chatPDF.git
```

2. Set up a Python virtual environment and install the required packages by running the setup script:

```shell
chmod +x setup.sh
./setup.sh
```

3. If the virtual environment is not active, activate it:

```shell
source .venv/bin/activate
```

4. Place the PDF file you want to use as the source of information for the chatbot in the project directory.

5. Update the `split_and_store.py` script to read your PDF file by changing the file path:

```python
with open('your-pdf-file-name.pdf', 'rb') as file:
```

6. Set up the OpenAI API key as an environment variable in a .env file in the project directory:

```shell
OPENAI_API_KEY=your_openai_api_key
```

7. Run the split_and_store.py script to split the PDF text into chunks and store them:

```shell
python split_and_store.py
```

8. Run the main.py script to start the chatbot:

```shell
python main.py
```

9. Enter your questions at the prompt, and the chatbot will provide answers based on the PDF content. To exit the chatbot, type 'quit' when prompted for a question.

10. When you're done, deactivate the virtual environment:

```shell
deactivate
```