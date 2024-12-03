import os
from dotenv import load_dotenv

load_dotenv()

GITBOOK_API = os.getenv('GITBOOK_API')


print(f"GITBOOK API is: {GITBOOK_API}")
