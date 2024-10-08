from llama_index.readers.web import BeautifulSoupWebReader

reader = BeautifulSoupWebReader()

url = "https://en.wikipedia.org/wiki/Abraham_Lincoln"

documents = reader.load_data(urls=[url])
