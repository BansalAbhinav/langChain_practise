from langchain.text_splitter import RecursiveCharacterTextSplitter

text ='''
Large Language Models (LLMs) are advanced deep learning models trained on massive amounts of text data to understand and generate human-like language.
 They are typically built on transformer architectures, which use mechanisms like attention to capture relationships between words and context over long passages of text. 



 An LLM works by predicting the next word in a sequence, but due to its training on billions of sentences, it learns grammar, facts, reasoning patterns, and even some 
 problem-solving skills. The size of an LLM is measured in parameters, which are the weights learned during training, and larger models generally show stronger performance 
 but also require more computational resources. Modern LLMs are not only used for chatbots but also for tasks such as summarization, translation, code generation, 
 and knowledge retrieval. Despite their power LLMs have limitations such as hallucinations (producing false information), sensitivity to prompts, 
 and the need for careful alignment with user intent.
'''

splitters = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
)

chunks = splitters.split_text(text)
print(chunks[0])
print(len(chunks))