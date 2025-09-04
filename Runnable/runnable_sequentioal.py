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

prompt1 = PromptTemplate(
    template="Write a joke about{topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template="Explain the following joke {topic}",
    input_variables=['topic']
)

parser =StrOutputParser()
chain = prompt1 |model | parser | prompt2 |parser
chain = RunnableSequence(prompt1 , model, parser,prompt2,parser )

result= chain.invoke({'topic':'Ai'})

print(result)