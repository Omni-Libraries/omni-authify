# 🚀 FastAPI Integration for Facebook Login

Easily integrate Facebook OAuth2 authentication into your FastAPI project using Omni-Authify library. This guide will 
walk you through configuration, setting up API views, updating URLs, and best practices.

---

## ⚙️ Configure .env file

To use Omni-Authify in to your FastAPI project, You have to store provider-related credentials in an .env file to 
include Facebook and/or any other OAuth 
providers.

### **.env file**
```dotenv
OMNI_AUTHIFY_ENABLED_PROVIDERS=facebook,linkedin

FACEBOOK_CLIENT_ID=600908255789503
FACEBOOK_CLIENT_SECRET=250d0f2964234d733bd4f88a037a58c9
FACEBOOK_REDIRECT_URI=https://7630-213-230-116-226.ngrok-free.app/facebook/callback
FACEBOOK_STATE='your_strong_state'
FACEBOOK_SCOPE='email,public_profile'
FACEBOOK_FIELDS='id,name,email,picture'

LINKEDIN_CLIENT_ID=your-linkedin-client-id
LINKEDIN_CLIENT_SECRET=your-linkedin-client-secret
LINKEDIN_REDIRECT_URI=http://localhost:8000/linkedin/callback
LINKEDIN_SCOPE=r_liteprofile,r_emailaddress

```
Go and take a look at the Facebook SetUP Guide to get Facebook related credentials!
- [Supported Providers and Frameworks](providers.md)

## RestAPI Views

Learn how to create API views to handle Facebook login and callback in your FastAPI application.

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

# Facebook Login API View
@app.get("/facebook/login")
def facebook_login():
    try:
        auth = OmniAuthifyFastAPI(provider_name="facebook")
        auth_url = auth.get_auth_url()
        return RedirectResponse(auth_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error initiating Facebook login: {str(e)}")

# Facebook Callback API View
@app.get("/facebook/callback")
def facebook_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="No code provided")

    try:
        auth = OmniAuthifyFastAPI(provider_name="facebook")
        user_info = auth.get_user_info(code)
        # TODO: Authenticate/login the user and save the user_info
        return {"message": "User authenticated successfully", "user_info": user_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing Facebook callback: {str(e)}")
```

---

## ✅ Best Practices

- **🔒 Use Environment Variables**: Always use environment variables to store important information like `client_id` and `client_secret`. This helps keep your credentials safe 🛡️.
- **🔗 Match Redirect URI**: Make sure the `redirect_uri` is consistent between your Facebook App settings and your code to avoid errors 🚫.

---

**Omni-Authify** makes adding Facebook authentication to your Django REST Framework app straightforward and secure. Follow these steps and best practices to provide your users with a seamless login experience. 🚀✨

