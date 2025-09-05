from langchain_community.document_loaders import WebBaseLoader



# loader = WebBaseLoader(url)
# docs = loader.load()
# print(len(docs))
# print('\n')
# print(docs)




# connecting a llm 

from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
load_dotenv()
url = "https://www.amazon.in/Smartchoice-300Nits-Xd0020ax-Tempest-Cooling/dp/B0CCVZP835/ref=sr_1_6?crid=MS641VJOTIS3&dib=eyJ2IjoiMSJ9.JeZI9x71ALfrPlAsOHxR0_91H6s1AZGQu-LYYAED5ksZtt0QtPsfTLlMVIlUhd5oF4ecLY5oaXY8f5tOrACr-JddiElkCv8yRNaUfNXYGyTTNIbIUdu8fCSt4jV6W0Bz6oMgHesjIPogx4Pv01ekOulFsclt7F9z8ahVfC-mFqtssaOiCmrDLzxIaoTNOVyjkHRyYuMCpAPAD4LlUyaWHBxnAfF18PtTVHBYSeQI-8U.W_19YdwPW6a4rhQ1GLDmpCrfPCYOV-qQG9t6j6Ijxms&dib_tag=se&keywords=laptop+4060&qid=1757085206&sprefix=laptop+060%2Caps%2C262&sr=8-6"

llm= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

parser =StrOutputParser()
prompt = PromptTemplate(
    template="answer the follwing {question} from  {topic}",
    input_variables=['question','topic']
)
loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model |parser

result = chain.invoke({'question':"tell me gpc cpu and ram and display quality of the laptop only this details","topic":docs[0].page_content})
print(result)
