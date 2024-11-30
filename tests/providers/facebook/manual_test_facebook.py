from omni_authify import settings
from omni_authify.providers.facebook import Facebook

client_id = settings.client_id
client_secret = settings.client_secret
redirect_uri = settings.redirect_uri

provider = Facebook(client_id, client_secret, redirect_uri, fields = "public_profile,email")
fields = "id,name,email,birthday,friends"

# ==== Step 1: Get the authorization URL ====
auth_url = provider.get_authorization_url(state='test_state')
print(f"Visit this URL to authorize: {auth_url}")

# ==== Step 2: User authorizes and gets redirected to your redirect_uri with a 'code' parameter ====
code = input("Enter the 'code' parameter from the URL you were redirected to: ")

# ==== Step 3: Exchange the code for an access token ====
access_token = provider.get_access_token(code)
print(f"Access Token: {access_token}")

# ==== Step 4: Get the user's profile ====
user_info = provider.get_user_profile(access_token, fields=fields)
print(f"User Info: {user_info}")




