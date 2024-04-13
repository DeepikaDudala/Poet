import streamlit as st
import requests

def get_openai_respone(input_text):
    responses = requests.post('http://localhost:8000/poemByOpenAI/invoke',json={"input":{'topic':input_text}})
    return responses.json()['output']['content']

def get_ollama_respone(input_text):
    responses = requests.post('http://localhost:8000/poemByOllama/invoke',json={"input":{'topic':input_text}})
    return responses.json()['output']

st.title("Langchain Demo with LLaMa2 and OpenAI")
st.write("This is a simple app that uses Langchain API to generate poems using OpenAI and Ollama.")

input_text1 = st.text_input("write a poem on ")
if st.button("Generate Poem Using OpenAI"):
    st.write(get_openai_respone(input_text1))

input_text2 = st.text_input("write a poem on")
if st.button("Generate Poem Using Ollama"):
    st.write(get_ollama_respone(input_text2))

