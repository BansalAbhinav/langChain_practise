from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage
#chat Temaplte
chat_template=ChatPromptTemplate([
      ('system','You are a helpful ai asssitant expert'),
        MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

#load chat History
chat_history = []
with open ('chat_history.txt') as f:
        chat_history.extend(f.readlines())

print(chat_history)
#create a prompt 

prompt= chat_template.invoke({'chat_history':chat_history,'query':"Where is my refund"})

print(prompt)