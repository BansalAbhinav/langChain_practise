from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system','You are a helpt ai asssitant expert in {domain}'),
    ('human','Explain in simple terms , what is {topic}')
  
])

prompt= chat_template({'domain':'Gaming expert pc','topic':'dying light beast'})

print(prompt)