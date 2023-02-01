import os
from dotenv import load_dotenv

load_dotenv()

class GoogleCSE:
    base_url = 'https://www.googleapis.com/customsearch/v1/siterestrict?'
    key = os.environ.get('GOOGLE_CSE_KEY')
    cx = os.environ.get('GOOGLE_CX')
