from langchain_groq import ChatGroq
from langchain_core.tools import tool
import os 
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",   
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

@tool
def add_num (x:int  , y:int ) -> int :
    """Return the sum of two numbers.""" 
    return x+y

print(add_num.invoke({"x":4 , "y":1}))

#Bind to llm
llm = model.bind_tools([add_num])
query= "What is the sum of 2 and 3?"
result = llm.invoke(query)

tool_output = add_num.invoke(result.tool_calls[0])    
print("Tool output:", tool_output.content)


# ToolMessage object
# - content
# - name
# - tool_call_id


