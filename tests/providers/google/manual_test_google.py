import sys
import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
print(BASE_DIR)
sys.path.insert(0, os.path.abspath(BASE_DIR))


import webbrowser

from omni_authify.providers.google import Google

from dotenv import load_dotenv

load_dotenv()


CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
SCOPE = "openid email profile"

provider = Google(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)

try:
    auth_url = provider.get_authorization_url(state="test")
    print("Authorization URL:", auth_url)
    
    webbrowser.open(auth_url)
    access_token = input("Input access token: ")

    profile = provider.get_user_profile(access_token)
    print("Profile user:", profile)
    
except Exception as e:
    print("Error:", e)