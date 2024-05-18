# CHAT PDF

## Description

This is a simple chat application that allows users to chat with PDF files and ask questions about the PDF files. The chat application is built using flask, streamlit, Langchain, OpenAI,
AWS S3.

Here Users can upload PDF files and ask questions about the PDF files. Users can get answers that are available in the PDF files. If the answer is not available in the PDF files, then the answer is generated using OPENAI API model GPT-3.5.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## Demo
### System Design
 ![SystemDesign](https://media.discordapp.net/attachments/1142888467920064672/1241301808006172683/image.png?ex=6649b3e5&is=66486265&hm=f586c5259bc20988e10b19484b742023d50e0f660d72c4ad0827c8abe8860dd4&=&format=webp&quality=lossless&width=1375&height=676) 

### UI
 ![UI](https://media.discordapp.net/attachments/1142888467920064672/1241302055973421107/image.png?ex=6649b420&is=664862a0&hm=b62393063ee9bd7a46335c309ef5b6bcf5d93bdfb0abf27d2602573bf1bc5eb1&=&format=webp&quality=lossless&width=1375&height=676) 


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Project Status

This project is currently in development. Users can upload PDF files and ask questions about the PDF files. Users can get answers that are available in the PDF files. If the answer is not available in the PDF files, then the answer is generated using OPENAI API model GPT-3.5.

## Future Scope

- Add more features
- Improve UI/UX
- Add more models

## Links and Resources

- [AWS S3](https://aws.amazon.com/s3/)
- [huggingface](https://huggingface.co/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Langchain](https://python.langchain.com/docs/get_started/quickstart)
- [OpenAI](https://openai.com/)
- [Streamlit](https://streamlit.io/)
- [Instructor-XL Model](https://huggingface.co/hkunlp/instructor-xl)
- [Text Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [Sentence Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

