import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GENAI_API_KEY")

llm = ChatGoogleGenerativeAI(
    api_key = api_key,
    model="gemini-2.5-pro"
)

prompt = ChatPromptTemplate.from_template("You are an expert in literature. Answer the user's question: {question}")

chain = prompt | llm | StrOutputParser()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chain.invoke({"question": user_input})
    print(f"Bot: {response}")