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
 ![SystemDesign](https://media.discordapp.net/attachments/796397516643368961/1183076783814365226/PDF-LangChain.jpg?ex=6587051d&is=6574901d&hm=d31ac0940f9010c65e93dba7a0942d647ddf3b6706b66452e919b341a12ff950&=&format=webp&width=1218&height=676) 

### UI
 ![UI](https://media.discordapp.net/attachments/796397516643368961/1183076737152729148/image.png?ex=65870512&is=65749012&hm=f53382d22865dbcbf5d7142772f5daec146096b8ac2d293e4ffaee848525a658&=&format=webp&quality=lossless&width=1375&height=676) 


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

