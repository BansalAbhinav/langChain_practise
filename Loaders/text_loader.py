from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
load_dotenv()
llm= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)




# loader text code

# loader = TextLoader('anime_poem.txt',encoding='utf-8')
# docs=loader.load()
# # print(docs)
# # print(docs[0])
# # print(docs[0].page_content)
# # print(docs[0].metadata)


loader = TextLoader(file_path='anime_poem.txt',encoding='utf-8')
docs=loader.load()
# print(docs)
# print(docs[0])
# print(docs[0].page_content)
# print(docs[0].metadata)

prompt = PromptTemplate(
    template="give me a summary of this {topic}",
    input_variables=['topic']
)
parser = StrOutputParser()
chain = prompt | model | parser

result = chain.invoke({'topic':docs })
print(result)






