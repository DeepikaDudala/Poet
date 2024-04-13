from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app =FastAPI(
    title="Langchain Server",
    description="A simple API server",
    version="0.1"
)

add_routes(app,ChatOpenAI(),path='/openai')

#Defining Models
model1 = ChatOpenAI()
model2 = Ollama(model="llama2")

#Adding Promts
promt1 = ChatPromptTemplate.from_template("write a poem on {topic} with in  4 lines")
promt2 = ChatPromptTemplate.from_template("write a poem on {topic} with in 4 lines")

add_routes(app,promt1 | model1,path='/poemByOpenAI')
add_routes(app,promt2 | model2, path='/poemByOllama')    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
