import os
from dotenv import load_dotenv
from llama_index.readers.web import BeautifulSoupWebReader
from llama_index.core import VectorStoreIndex

def main(url: str) -> None:
    reader = BeautifulSoupWebReader()
    documents = reader.load_data(urls=[url])
    print(f"Loaded {len(documents)} document(s)")
    
    index = VectorStoreIndex.from_documents(documents)
    print("Index created successfully")
    
    query_engine = index.as_query_engine()
    
    response = query_engine.query("What is LlamaIndex?")
    print("\nQuery Response:")
    print(response)

if __name__ == '__main__':
    load_dotenv()
    print('Hello, World LlamaIndex!')
    print(f"OPENAI_API_KEY is: {os.environ['OPENAI_API_KEY']}")
    print('**********')
    main(url='https://medium.com/codex/an-overview-of-the-llamaindex-framework-9ee9db787d16')