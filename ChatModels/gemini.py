from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', 
                               api_key=os.getenv('GEMINI_API_KEY'),temperature=0)
result = model.invoke('What is supervised Learning? ')

print(result.content)