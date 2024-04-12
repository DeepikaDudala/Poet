from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

#promt template
promt = ChatPromptTemplate.from_messages([
    ("system","you are a helpful AI assistant that can answer questions about programming and software development."),
    ("human","Question : {question}")
])

#streamlit app
st.title("Langchain Ollama")
st.write("This is a simple app that uses Ollama's GPT-3 to answer questions about programming and software development.")

#Ollama llm
llm = Ollama(model='llama2')

output_parser = StrOutputParser()

chain = promt | llm | output_parser

question = st.text_input("Enter your question here")

if st.button("Ask"):
    st.write(chain.invoke(question))
