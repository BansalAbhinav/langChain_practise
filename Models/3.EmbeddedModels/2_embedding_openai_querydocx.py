from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
document=[
    "delhi is capital of india"
    "doon is capital of uttarakhand"
]
result=embedding.embed_documents(document)
print(str(result))