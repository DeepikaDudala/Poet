import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


#Promt template
promt = ChatPromptTemplate.from_messages([
    ("system","you are a helpful AI assistant that can answer questions in oneline"),
    ("human","Question : {question}")
])


#streamlit app
st.title("Langchain OpenAI")
st.write("This is a simple app that uses OpenAI's GPT-3 to answer questions about programming and software development.")
st.write("Please enter your question below and I will try to answer it.")
question = st.text_input("Enter your question here")

#openai LLm
llm = ChatOpenAI(model='gpt-3.5-turbo-0125',temperature=0.7)
output_parser = StrOutputParser()
chain = promt | llm | output_parser

if st.button("Ask"):
    st.write(chain.invoke(input=question))