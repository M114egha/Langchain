from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import os 
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",   
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


@tool
def add_num(x:int , y:int) -> int:
    """Returns the addition of given two inputs"""
    return   x+y

@tool
def multiply_num(x:int , y:int)-> int:
    """Return th emultiplication of given two inputs"""
    return x*y

@tool
def div_num(x:int , y:int)->int :
    """Returns the division of given two inputs"""
    if y == 0 :
        return "Cannot divide by zero"
    else :
        return x/y
    
tools=[add_num , multiply_num , div_num]
llm = model.bind_tools(tools)

chat_history = []

print("Type 'exit' to end the conversation")

while  True:
    query= input("Enter your query")

    if query.lower() == 'exit':
        break

    # Add user input
    chat_history.append(HumanMessage(content=query))

    result = llm.invoke(chat_history)
    chat_history.append(result)
    


