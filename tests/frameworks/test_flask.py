from flask import Flask, redirect, request

from omni_authify.providers.facebook import Facebook

app = Flask(__name__)

# Replace with your actual app credentials
FACEBOOK_CLIENT_ID = "your-client-id"
FACEBOOK_CLIENT_SECRET = "your-client-secret"
REDIRECT_URI = "http://localhost:5000/callback"

facebook = Facebook(FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET, REDIRECT_URI)

@app.route("/login")
def login():
    return redirect(facebook.get_authorization_url())

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return {"error": "No code provided"}, 400

    # Exchange code for token
    token_data = facebook.get_access_token(code)
    access_token = token_data["access_token"]

    # Get user profile
    user_data = facebook.get_user_profile(access_token)
    return user_data
