from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
load_dotenv()
#google/gemma-2-2b-it
#SmolLM3-3B
#ethzanalytics/distilgpt2-tiny-conversational
llm= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

schema = [ 
    ResponseSchema(name='fact_1',description="Fact 1 about the topic"),
    ResponseSchema(name='fact_2',description="Fact 2 about the topic"),
    ResponseSchema(name='fact_3',description="Fact 3 about the topic"),
    ResponseSchema(name='fact_4',description="Fact 4 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'give 3 fact about {topic} \n {format_instruction}',
    input_types=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain = template | model | parser
chain_result = chain.invoke({'topic':"black hole"})

propmt = template.invoke({'topic':"black Hole"})
result = model.invoke(propmt)
final_result = parser.parse(result.content)

print(final_result)


