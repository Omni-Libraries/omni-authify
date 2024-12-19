# 🚀 FastAPI Integration for Oauth2 authentication

Easily integrate OAuth2 authentication into your FastAPI project using Omni-Authify library. This guide will 
walk you through configuration, setting up API views, updating URLs, and best practices.

---

## ⚙️ Configure .env file

To use Omni-Authify in to your FastAPI project, You have to store provider-related credentials in an .env file to 
include Facebook, GitHub, Google and/or any other OAuth 
providers.

### **.env file**
```dotenv
OMNI_AUTHIFY_ENABLED_PROVIDERS=facebook,linkedin

FACEBOOK_CLIENT_ID=your-facebook-client-id
FACEBOOK_CLIENT_SECRET=your-facebook-client-secret
FACEBOOK_REDIRECT_URI=https:/localhost:8000/facebook/callback
FACEBOOK_STATE='your_strong_state'
FACEBOOK_SCOPE='email,public_profile'
FACEBOOK_FIELDS='id,name,email,picture'

GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
GITHUB_REDIRECT_URI=https://localhost:8000/github/callback
GITHUB_SCOPE=user,repo

GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=https://localhost:8000/google/callback
GOOGLE_STATE=your-strong-state
GOOGLE_SCOPES='openid profile email https://www.googleapis.com/auth/contacts.readonly' # Don't seperate the fields with commas

```
Go and take a look at the Providers SetUP Guide to get Provider related credentials!
- [Supported Providers and Frameworks](providers.md)

## RestAPI Views

Learn how to create API views to handle Provider login and callback in your FastAPI application.

### 📝 Prerequisites

- **Installation**: Install Omni-Authify with FastAPI framework support using the following command:

  ```bash
  pip install omni-authify[fastapi]
  ```

- **FastAPI version: 0.115.0 or higher**
- **FastAPI installed**
- Omni-Authify installed and configured (see [Installation Guide](installation.md))

### 🚀 Setting Up API Views

Create API views to handle the login and callback processes.

```python
# Omni-Authify Integration with FastAPI

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Optional

from omni_authify.frameworks.fastapi import OmniAuthifyFastAPI

app = FastAPI()

# ======== Facebook Login ========
@app.get("/facebook/login")
def facebook_login():
    try:
        auth = OmniAuthifyFastAPI(provider_name="facebook")
        auth_url = auth.get_auth_url()
        return RedirectResponse(auth_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error initiating Facebook login: {str(e)}")

@app.get("/facebook/callback")
def facebook_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="No code provided")

    try:
        auth = OmniAuthifyFastAPI(provider_name="facebook")
        user_info = auth.get_user_info(code)
        print(f"User Info: {user_info}")
        
        # TODO: Authenticate/login the user and save the user_info
        return {"message": "User authenticated successfully", "user_info": user_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing Facebook callback: {str(e)}")

# ======== GitHub Login ========
@app.get("/github/login")
def facebook_login():
    try:
        auth = OmniAuthifyFastAPI(provider_name="github")
        auth_url = auth.get_auth_url()
        return RedirectResponse(auth_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error initiating Facebook login: {str(e)}")

@app.get("/github/callback")
def facebook_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="No code provided")

    try:
        auth = OmniAuthifyFastAPI(provider_name="github")
        user_info = auth.get_user_info(code)
        print(f"User Info: {user_info}")
        
        # TODO: Authenticate/login the user and save the user_info
        return {"message": "User authenticated successfully", "user_info": user_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing GitHub callback: {str(e)}")


# ======== Google Login ========
@app.get("/google/login")
def facebook_login():
    try:
        auth = OmniAuthifyFastAPI(provider_name="github")
        auth_url = auth.get_auth_url()
        return RedirectResponse(auth_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error initiating Google login: {str(e)}")

@app.get("/google/callback")
def facebook_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="No code provided")

    try:
        auth = OmniAuthifyFastAPI(provider_name="github")
        user_info = auth.get_user_info(code)
        print(f"User Info: {user_info}")
        
        # TODO: Authenticate/login the user and save the user_info
        return {"message": "User authenticated successfully", "user_info": user_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing Google callback: {str(e)}")
```

---

## ✅ Best Practices

- **🔒 Use Environment Variables**: Always use environment variables to store important information like `client_id` and `client_secret`. This helps keep your credentials safe 🛡️.
- **🔗 Match Redirect URI**: Make sure the `redirect_uri` is consistent between your Provider App settings and your code to avoid errors 🚫.

---

**Omni-Authify** makes adding Oauth2 authentication to your RESTAPI app straightforward and blazingly fast. 
Follow these steps and best practices to provide your users with a seamless login experience. 🚀✨

