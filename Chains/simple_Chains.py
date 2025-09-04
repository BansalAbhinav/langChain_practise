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

prompt = PromptTemplate(
    template = 'Genertae 5 intersinting facts about{topic}',
    input_variables=['topic']

)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt | model | parser

# result=chain.invoke({'topic':'cricket '})
# print(result)

chain.get_graph().print_ascii()