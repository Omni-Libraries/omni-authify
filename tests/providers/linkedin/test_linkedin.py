from omni_authify import settings
from omni_authify.providers.linkedin import LinkedIn

client_id = settings.linkedin_client_id
client_secret = settings.linkedin_client_secret
redirect_uri = settings.linkedin_redirect_uri
scope = settings.linkedin_scopes

print(client_id, client_secret, redirect_uri, scope)


provider = LinkedIn(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
)

# ==== Step 1: Get the authorization URL ====
auth_url = provider.get_authorization_url(state='linkedin_test_state')
print(f"Visit this URL to authorize: {auth_url}")

# ==== Step 2: User authorizes and gets redirected to your redirect_uri with a 'code' parameter ====
code = input("Enter the 'code' parameter from the URL you were redirected to: ")

# ==== Step 3: Exchange the code for an access token ====
access_token = provider.get_access_token(code)
print(f"Access Token: {access_token}")

# ==== Step 5: Get the user's profile ====
user_info = provider.get_user_profile(access_token, fields=scope)
print(f"User Info: {user_info}")


