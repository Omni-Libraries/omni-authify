import os

from dotenv import load_dotenv

load_dotenv()

facebook_client_id = os.getenv('FACEBOOK_CLIENT_ID')
facebook_client_secret = os.getenv('FACEBOOK_CLIENT_SECRET')
facebook_redirect_uri = os.getenv('FACEBOOK_REDIRECT_URI')

github_client_id = os.getenv('GITHUB_CLIENT_ID')
github_client_secret = os.getenv('GITHUB_CLIENT_SECRET')
github_redirect_uri = os.getenv('GITHUB_REDIRECT_URI')

google_client_id = os.getenv('GOOGLE_CLIENT_ID')
google_client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
google_redirect_uri = os.getenv('GOOGLE_REDIRECT_URI')
google_scopes = os.getenv('GOOGLE_SCOPES')

