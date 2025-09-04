from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from typing import TypedDict, Annotated,Optional,Literal
from pydantic import BaseModel,Field 
llm= HuggingFacePipeline.from_model_id(
    model_id="distilgpt2",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

#Schema
class Review(BaseModel):

    key_themes:list[str] = Field(description="Write down all the discussed in the review in a list")
    summary: str = Field(description="A brief Summary of review")
    sentiment: Literal["pos","neg"] = Field(description="return sentimaent of the review ")
    pros:Optional[list[str]] = Field(default=None , description="write doen all pros inside a list")
    cons:Optional[list[str]] = Field(default=None , description="write doen all cons inside a list")

    # key_themes: Annotated[list[str],"Write down all the discussed in the review in a list "]
    # summary:Annotated[str,"A brief Summary of review"]
    # sentiment:Annotated[Literal["pros","neg"],"return sentimaent of the review "]
    # pros:Annotated[Optional[list[str]],"write doen all pros inside a list"]
    # cons:Annotated[Optional[list[str]],"write doen all cons inside a list"]



Structured_model = model.with_structured_output(Review)


result = Structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")
print(result)