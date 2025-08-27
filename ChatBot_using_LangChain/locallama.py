from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

##for langsmith tracing
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##Prompt Template
prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a helpful assistant.Please respond to the user's question."),
  ("user", "Question: {question}")
])


##Streamlit framework
st.title('Langchain Demo Chatbot with Ollama LLM') 
input_text = st.text_input("Ask a question:")

##Ollama LLM
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain=prompt | llm | output_parser 

if input_text:
  st.write(chain.invoke({"question" : input_text}))