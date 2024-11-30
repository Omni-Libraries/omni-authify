# Django REST Framework (DRF) Integration for Facebook Login

Easily integrate Facebook OAuth2 authentication into your Django REST Framework project using Omni-Authify. This guide will walk you through configuration, setting up API views, updating URLs, and best practices.

---

## ⚙️ Configure Settings

Add the Omni-Authify settings to your Django project settings to include Facebook and/or any other OAuth providers.

```python
import os

OMNI_AUTHIFY = {
    'HOME_PAGE': {
        'dashboard': {
            'home': 'the-page_name-where-you-redirect-the-user-after-authentication-and-login'
        }
    },
      
    'PROVIDERS': {
        'facebook': {
            'client_id': os.getenv('FACEBOOK_CLIENT_ID'),
            'client_secret': os.getenv('FACEBOOK_CLIENT_SECRET'),
            'redirect_uri': '🌐http://localhost:8000/facebook/callback',
            'state': 'your-unguessable-state', # optional
            'fields': 'email,public_profile...'
        },
        # Add other providers here if needed
    }
}
```

---

## DRF API Views

Learn how to create API views to handle Facebook login and callback in your Django REST Framework application.

### 📝 Prerequisites

- **Installation**: Install Omni-Authify with Django REST Framework support using the following command:

  ```bash
  pip install omni-authify[drf]
  ```

- **Django 2.2 or higher**
- **Django REST Framework installed**
- Omni-Authify installed and configured (see [Installation Guide](installation.md))

### 🚀 Setting Up API Views

Create API views to handle the login and callback processes.

#### **views.py**

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from omni_authify.providers.facebook import Facebook

import os
from dotenv import load_dotenv

load_dotenv()

class FacebookLoginAPIView(APIView):
    def get(self, request):
        # === Initialize the provider with environment variables ====
        facebook_provider = Facebook(
            client_id=os.getenv('FACEBOOK_CLIENT_ID'),
            client_secret=os.getenv('FACEBOOK_CLIENT_SECRET'),
            redirect_uri=os.getenv('FACEBOOK_REDIRECT_URI'),
            fields=os.getenv('FACEBOOK_USER_FIELDS')
        )
        # ==== Generate authorization URL and return it in the response ====
        auth_url = facebook_provider.get_authorization_url(state='your_random_state')
        return Response({'auth_url': auth_url}, status=status.HTTP_200_OK)

class FacebookCallbackAPIView(APIView):
    def get(self, request):
        # ==== Get authorization code from the request ====
        code = request.GET.get('code')
        if not code:
            return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # ==== Initialize the provider with environment variables ====
            facebook_provider = Facebook(
                client_id=os.getenv('FACEBOOK_CLIENT_ID'),
                client_secret=os.getenv('FACEBOOK_CLIENT_SECRET'),
                redirect_uri=os.getenv('FACEBOOK_REDIRECT_URI'),
                fields=os.getenv('FACEBOOK_USER_FIELDS')
            )
            # ==== Exchange code for access token ====
            access_token = facebook_provider.get_access_token(code)
            # ==== Fetch user profile information ====
            user_info = facebook_provider.get_user_profile(access_token)
            # TODO: Authenticate the user and return a token
            return Response({'user_info': user_info}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

---

### 🔁 Alternative Implementation

#### **views.py (Alternative Approach)**

This version uses the OmniAuthifyDRF helper class for an easier implementation.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from omni_authify.frameworks.drf import OmniAuthifyDRF

class FacebookLoginAPIView(APIView):
    def get(self, request):
        auth = OmniAuthifyDRF(provider_name='facebook')
        auth_url = auth.get_auth_url()
        return Response({'auth_url': auth_url}, status=status.HTTP_200_OK)

class FacebookCallbackAPIView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            auth = OmniAuthifyDRF(provider_name='facebook')
            user_info = auth.get_user_info(code)
            # Todo: Authenticate/login the user and save the user_info on your own! or make auto_authenticate True
            return Response({'message': 'User authenticated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

---

## 🌐 Update URLs

Add the login and callback views to your app's **urls.py** file:

```python
# urls.py

from django.urls import path
from .views import FacebookLoginAPIView, FacebookCallbackAPIView

urlpatterns = [
    path('facebook/login/', FacebookLoginAPIView.as_view(), name='facebook_login'),
    path('facebook/callback/', FacebookCallbackAPIView.as_view(), name='facebook_callback'),
]
```

---

## ✅ Best Practices

- **🔒 Use Environment Variables**: Always use environment variables to store important information like `client_id` and `client_secret`. This helps keep your credentials safe 🛡️.
- **🔗 Match Redirect URI**: Make sure the `redirect_uri` is consistent between your Facebook App settings and your code to avoid errors 🚫.

---

**Omni-Authify** makes adding Facebook authentication to your Django REST Framework app straightforward and secure. Follow these steps and best practices to provide your users with a seamless login experience. 🚀✨

