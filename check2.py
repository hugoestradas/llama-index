from llama_index.readers.web import BeautifulSoupWebReader

# Initialize the reader
reader = BeautifulSoupWebReader()

# Define the URL to read
url = "https://en.wikipedia.org/wiki/Abraham_Lincoln"

# Load the data
documents = reader.load_data(urls=[url])

# Now you can use these documents for indexing and querying with LlamaIndex