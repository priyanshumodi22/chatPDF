import streamlit as st
import time
from dotenv import load_dotenv
from decouple import config
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
import base64
from pathlib import Path
from streamlit_javascript import st_javascript
# from st_files_connection import FilesConnection
import boto3
from io import BytesIO
import os

OPENAI_API_KEY = config('OPENAI_API_KEY')

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = config('AWS_SECRET_KEY_ID')

st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon="📚", layout="wide")

ui_width =  st_javascript("window.innerWidth")

col1,col2 = st.columns(spec=[2,2] , gap= "small")

curr_path = os.getcwd()
s3 = boto3.client(
                service_name='s3',
                region_name='ap-south-1',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
            )

bucket = "majorbucket106"

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    # Display an acknowledgment spinner
    with st.spinner("Fetching response..."):
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']

        # Reverse the order of messages to display recent chats on top
        reversed_chat_history = reversed(st.session_state.chat_history)

        for i, message in enumerate(reversed_chat_history):
            if i % 2 == 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
        
        # time.sleep(20)


def displayPDF(file,ui_width):
    d = file.read()
    base64_pdf = base64.b64encode(d).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height={str(ui_width*4/3)} type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

with col1:
        st.subheader("PDFs")

def main():
    load_dotenv()
    st.write(css, unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'",accept_multiple_files=True, type=["pdf"])
        
        with col1:
            for pdf in pdf_docs:
                s3.upload_fileobj(pdf, bucket, pdf.name)
                # pdf.seek(0)
                with st.expander(pdf.name):
                    displayPDF(pdf,ui_width - 50)
        

        # Display a progress bar for PDF upload
        # if pdf_docs:
        #     for pdf in pdf_docs:
        #         print("Uploaded to S3")
        #         s3.upload_fileobj(pdf, bucket, pdf.name)
        if pdf_docs:
            # get pdf text
            raw_text = get_pdf_text(pdf_docs)

            #  upload to s3

            # get the text chunks
            text_chunks = get_text_chunks(raw_text)

            # create vector store
            vectorstore = get_vectorstore(text_chunks)

            # create conversation chain
            st.session_state.conversation = get_conversation_chain(
                vectorstore)
            
            # st.success("PDFs uploaded successfully! Click on 'Process' to start processing.", icon="✅")
            # st.session_state["processed_pdfs"] = pdf_docs
            
            
            st.success("Processing completed! You can now chat with PDF.", icon="✅")


    with col2:
        if "conversation" not in st.session_state:
            st.session_state.conversation = None
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = None

        st.subheader("Ask question: ")

        user_question = st.text_input("Ask a question about your documents:")
        with st.expander("Chat history"):
         with st.container():
            if user_question:
            # Handle user input and display acknowledgment spinner
                handle_userinput(user_question)


if __name__ == '__main__':
    main()
