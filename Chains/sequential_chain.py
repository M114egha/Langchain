from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
import os 
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",   
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

prompt_explain = PromptTemplate(
    input_variables=["concept"],
    template="Explain the {concept} in detail in 100-200 words."
)

prompt_summarize = PromptTemplate(
    input_variables=["text"],
    template="Summarize the exaplanation into 5 points."
)


#to_dict = RunnableLambda(lambda x: {"text": x})
parser=StrOutputParser()


chain = prompt_explain | llm | parser  | prompt_summarize | llm | parser
result =chain.invoke({"concept":"photosynethesis"})

print(result)




