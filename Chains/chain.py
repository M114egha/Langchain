from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",   
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

prompt = ChatPromptTemplate.from_messages(
    [("system" , "You are an helpful assistant "),
     ("human , {user_query}"),
     ("ai", "Let me help me you .")
    ]
    )

parser= StrOutputParser()

chain= prompt | llm  | parser

result = chain.invoke({"user_query":"What is the capital of India?"})

print(result)

 