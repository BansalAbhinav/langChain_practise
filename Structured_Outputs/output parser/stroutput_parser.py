from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate
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

 

prompt1 = template1.invoke({'topic':'black Hole'})
result=model.invoke(prompt1)
prompt2 = template2.invoke({'text':result.content})
result2=model.invoke(prompt2)
print(result2.content)