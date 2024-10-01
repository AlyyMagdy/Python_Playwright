import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access environment variables
database_url = os.getenv('BROWSER')
# api_key = os.getenv('API_KEY')
# debug = os.getenv('DEBUG')

print(f"Database URL: {database_url}")
# print(f"API Key: {api_key}")
# print(f"Debug mode: {debug}")
