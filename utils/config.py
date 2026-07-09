import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VT_API_KEY")
print(API_KEY)