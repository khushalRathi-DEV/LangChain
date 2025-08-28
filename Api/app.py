from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_groq import ChatGroq
##from langchain_community.llms import Ollama
import uvicorn 
import os

from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

app = FastAPI(
  title = 'Langchain Server',
  version = "1.0",
  description="A simple Langchain Server",
)

# add_routes(
#   app,
#   ChatOpenAI(),
#   path="/openai"
# )

# model=ChatOpenAI()
#groq model
llm=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
)

prompt1 = ChatPromptTemplate.from_template("Write a short story about {topic} in 50 words")
prompt2 = ChatPromptTemplate.from_template("Write a short poem about {topic} in 50 words")
prompt3 = ChatPromptTemplate.from_template("tell me a small joke about {topic}")

add_routes(
  app,
  prompt1|llm,
  path="/story"
)

add_routes(
  app,
  prompt2|llm,
  path="/poem"
)

add_routes(
  app,
  prompt3|llm,
  path="/joke"
)

if __name__ == "__main__":
  uvicorn.run(app, host="localhost", port=8000)
