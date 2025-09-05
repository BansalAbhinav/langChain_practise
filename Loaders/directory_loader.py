from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader,TextLoader

loader = DirectoryLoader(
    path="multiple-pdf-folder",
    glob=['*.pdf','*.txt'],
    loader_cls=PyPDFLoader
)

docs =loader.load()
# print(docs[0].page_content)
# print(docs[0].metadata)


#lazy load
docss =loader.lazy_load()
for document in docss:
    print(document.page_content)
