from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
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
    template="Explain the following joke in 2 lines {topic}",
    input_variables=['topic']
)

parser =StrOutputParser()
joke_generator=RunnableSequence(prompt1,model,parser)
parallel_chain =RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_generator,parallel_chain)
result= final_chain.invoke({'topic':'cricket'})

print(result)