import os
from dotenv import load_dotenv

# Ensure you have the correct import based on your llama_index version
try:
    from llama_index.readers.web import BeautifulSoupWebReader
except ImportError:
    print("Could not import BeautifulSoupWebReader. Please check your llama_index installation.")

# Assuming the rest of your code follows here...
