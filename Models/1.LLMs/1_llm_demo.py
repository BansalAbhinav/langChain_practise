from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm=OpenAI(model="gpt-3.5-turbo-instruct")
#Invke is used for send ing query back to our llm model
result=llm.invoke("What is the capital of india") 
print(result)