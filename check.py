import os
from dotenv import load_dotenv

try:
    from llama_index.readers.web import BeautifulSoupWebReader
except ImportError:
    print("Could not import BeautifulSoupWebReader. Please check your llama_index installation.")
