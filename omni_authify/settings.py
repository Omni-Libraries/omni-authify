import os

from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('FACEBOOK_CLIENT_ID')
client_secret = os.getenv('FACEBOOK_CLIENT_SECRET')
redirect_uri = os.getenv('FACEBOOK_REDIRECT_URI')

