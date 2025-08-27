from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

##for langsmith tracing
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##Prompt Template
prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a helpful assistant.Please respond to the user's question."),
  ("user", "Question: {question}")
])

##Streamlit Framework
st.title("Langchain Demo Chatbot with Groq LLM")
input_text = st.text_input("Ask a question:")

##Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
)
output_parser = StrOutputParser()
chain=prompt | llm | output_parser

if input_text:
    response = chain.invoke(input_text)
    st.write(response)
