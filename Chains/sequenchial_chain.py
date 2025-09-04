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

prompt1 = PromptTemplate(
    template='Genertae a detailed report on {topic}',
    input_variables=['topic']

)

prompt2 = PromptTemplate(
    template="Generate 5 most imp points from this {report} ",
    input_variables=['report']

)
parser =StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'best games for pc'})
print(result)

chain.get_graph().print_ascii()