from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
load_dotenv()
#google/gemma-2-2b-it
#SmolLM3-3B
#ethzanalytics/distilgpt2-tiny-conversational
llm= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
llm2= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)


model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(
#  template='Classify the sentiment of the follwing text into positive or negative\n {feedback} \n {format_instruction}',
template=(
        "Classify the sentiment of the following text as either 'positive' or 'negative'.\n\n"
        "Text: {feedback}\n\n"
        "Return the answer strictly in this JSON format:\n"
        "{{\"sentiment\": \"positive\"}}\n\n"
        "If negative, return:\n"
        "{{\"sentiment\": \"negative\"}}"
    ),
 input_variables=['feedback'],

)

classifire_chain = prompt1 |model | parser2 

# clasifier_chain = prompt1 | model | parser
# result = classifire_chain.invoke({'text':"this is work wonderful but have slow performance "}).sentiment
# print(result)
prompt2 =PromptTemplate(
    template="Write and appropite respose to this positive feed back \n {feedback}",
    input_variables=['feedback']
)
prompt3 =PromptTemplate(
    template="Write and appropite respose to this negative feed back \n {feedback}",
    input_variables=['feedback']
)

   #(condition1,chain1)
    #(condition2,chain2)like if else 
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifire_chain |branch_chain

result2 = chain.invoke({'feedback':"this is a terrinle food "})

print(result2)
chain.get_graph().print_ascii()