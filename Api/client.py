import requests
import streamlit as st

def get_groq_response_story(input_text):
  response = requests.post(
    "http://localhost:8000/story/invoke",
    json={'input' : {'topic': input_text}}
  )

  return response.json()['output']['content']

def get_groq_response_poem(input_text):
  response = requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input' : {'topic': input_text}}
  )

  return response.json()['output']['content']

def get_groq_response_joke(input_text):
  response = requests.post(
    "http://localhost:8000/joke/invoke",
    json={'input' : {'topic': input_text}}
  )

  return response.json()['output']['content']


##streamlit framework
st.title('Langchain Demo Chatbot with Groq LLM')
input_text = st.text_input("Write the topic for the story:")
input_text1 = st.text_input("Write the topic for the poem:")
input_text2 = st.text_input("Write the topic for the joke:")

if input_text:
  st.write(get_groq_response_story(input_text))
if input_text1:  
  st.write(get_groq_response_poem(input_text1))
if input_text2:
  st.write(get_groq_response_joke(input_text2)) 

  