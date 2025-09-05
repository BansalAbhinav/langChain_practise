from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('Rest_Api.pdf')
docs = loader.load()
print(docs)
print(len(docs))