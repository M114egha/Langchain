from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import os 
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",   
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

prompt1= PromptTemplate(
    template = "Geanerate short  and simple notes from the given text \n{text}", 
    input_variables= ['text']
)

prompt2= PromptTemplate(
    template = " Generate 5 simple questions  from the following text \n {text}",
    input_variables=["text"]
)

prompt3= PromptTemplate(
    template= "Merge theprovided notes and quiz into single doc \n notes -> {notes} \n quiz -> {quiz}",
    input_variables=['notes' , 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | llm | parser ,
    'quiz': prompt2 | llm | parser
})

merge_chain= prompt3 |llm | parser 

chain = parallel_chain | merge_chain



text= """
In supervised learning, the algorithm learns to perform a task based on labeled examples provided during training. These labeled examples consist of input-output pairs, where the input is the data (features), and the output is the corresponding label or target variable. The goal of supervised learning is to generalize from the provided examples to make accurate predictions or decisions on new, unseen data. Since supervised learning algorithms are focused on learning a specific task or prediction, they are often referred to as “task-driven.” This term emphasizes that the algorithm’s learning process revolves around accomplishing a predefined task, guided by the labeled data."""
result = chain.invoke({'text': text})

print(result)