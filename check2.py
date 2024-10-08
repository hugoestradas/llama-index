from llama_index.readers.web import BeautifulSoupWebReader

reader = BeautifulSoupWebReader()

# Define the URL to read
url = "https://en.wikipedia.org/wiki/Abraham_Lincoln"

documents = reader.load_data(urls=[url])

