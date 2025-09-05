from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='test_csvfile.csv')
docs = loader.lazy_load()
# print(len(docs))
# print(docs[2].metadata)
# print(docs)

# for lazy loading use loops

for doc in docs:
    print(doc.page_content)