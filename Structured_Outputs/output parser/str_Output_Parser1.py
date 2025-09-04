from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
#google/gemma-2-2b-it
#SmolLM3-3B
#ethzanalytics/distilgpt2-tiny-conversational
llm= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
# /// thing todo **************==> topic -> LLM -> Detailed Report -> llm -> 5 lines summary   

# 1st prompt -> Detailed Report 

template1 = PromptTemplate(
  template="Write a detailed report on {topic}",
  input_variables=['topic']
 )
#2nd  prompt -> Summary 
template2 = PromptTemplate(
  template="Write a 5 line summary  on follwing texrt /n. {text}",
  input_variables=['text']
 )

parser = StrOutputParser()

chain =template1 | model | parser |template2 |model |parser

result =chain.invoke({'topic':'Black hole'})

print(result) 