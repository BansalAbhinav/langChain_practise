from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
#google/gemma-2-2b-it
#SmolLM3-3B
#ethzanalytics/distilgpt2-tiny-conversational
llm= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()
template = PromptTemplate(
    template = "Give me name , age and city of a fictioanl person \n {foramt_instruction}",
    input_variables=[],
    partial_variables={'foramt_instruction':parser.get_format_instructions()}

)
#normal way of writing -------------------------------
prompt = template.format()
result=model.invoke(prompt)
# print(result)
final_result= parser.parse(result.content)
# print(final_result)


#Chains way of writing -----------------------------------

chain = template | model | parser

result_chain = chain.invoke({})
print(result_chain)
