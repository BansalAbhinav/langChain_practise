from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
os.environ['hf_home'] = 'D:/huggingFace_cache'
llm= HuggingFacePipeline.from_model_id(
    model_id="distilgpt2",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)
result = llm.invoke("generate a paragph about react and  next js")
print(result)