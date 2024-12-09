import os

from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('FACEBOOK_CLIENT_ID')
client_secret = os.getenv('FACEBOOK_CLIENT_SECRET')
redirect_uri = os.getenv('FACEBOOK_REDIRECT_URI')


google_client_id = os.getenv('GOOGLE_CLIENT_ID')
google_client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
google_redirect_uri = os.getenv('GOOGLE_REDIRECT_URI')