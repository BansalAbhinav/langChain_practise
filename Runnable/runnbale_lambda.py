from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
load_dotenv()
llm= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template="Write a joke about{topic}",
    input_variables=['topic']
)


parser =StrOutputParser()
joke_generator=RunnableSequence(prompt1,model,parser)


parallel_chain =RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
    # 'word_count':RunnableLambda(lambda x : len(x.split()))

})

final_chain = RunnableSequence(joke_generator,parallel_chain)
result= final_chain.invoke({'topic':'cricket'})

final_result = """Joke -> {} \n Word Count -> {} """.format(result['joke'],result['word_count'])
print(final_result)