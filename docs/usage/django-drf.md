# Django REST Framework (DRF) Integration for Oauth2 authentication

Easily integrate multiple Providers Login into your Django REST Framework project using Omni-Authify. This guide 
will walk you through configuration, setting up API views, updating URLs, and best practices.

---

## ⚙️ Configure Settings

Add the Omni-Authify settings to your Django project settings to include Facebook, GitHub, Google and/or any other 
OAuth 
providers.

```python
import os
from dotenv import load_dotenv

load_dotenv()

OMNI_AUTHIFY = {
    'PROVIDERS': {
        'facebook': {
            'client_id': os.getenv('FACEBOOK_CLIENT_ID'),
            'client_secret': os.getenv('FACEBOOK_CLIENT_SECRET'),
            'redirect_uri': os.getenv('FACEBOOK_REDIRECT_URI'),
            'state': os.getenv('FACEBOOK_STATE'), # optional
            'scope': os.getenv('FACEBOOK_SCOPE'), # by default | add other FB app permissions you have!
            'fields': os.getenv('FACEBOOK_FIELDS'),
        },
        'github':{
            'client_id':os.getenv('GITHUB_CLIENT_ID'),
            'client_secret':os.getenv('GITHUB_CLIENT_SECRET'),
            'redirect_uri':os.getenv('GITHUB_REDIRECT_URI'),
            'state': os.getenv('GITHUB_STATE'),
            'scope':os.getenv('GITHUB_SCOPE'),
        },
        'google': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID'),
            'client_secret': os.getenv('GOOGLE_CLIENT_SECRET'),
            'redirect_uri': os.getenv('GOOGLE_REDIRECT_URI'),
            'state': os.getenv('GOOGLE_STATE'), # optional
            'scope': os.getenv('GOOGLE_SCOPES'),
        },
                
        # Add other providers here if needed
        'telegram': {
            # Coming....
        }
    }
}
```

---

## DRF API Views

Learn how to create API views to handle multiple Providers login and callback in your Django REST Framework application.

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
This version uses the OmniAuthifyDRF helper class for an easier implementation.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from omni_authify.frameworks.drf import OmniAuthifyDRF

# ======== Facebook Login ========
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
            print(f"User Info: {user_info}")
            
            # Todo: Authenticate/login the user and save the user_info on your own! or make auto_authenticate True
            return Response({'message': 'User authenticated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ======== GitHub Login ========
class GitHubLoginAPIView(APIView):
    def get(self, request):
        auth = OmniAuthifyDRF(provider_name='github')
        auth_url = auth.get_auth_url()
        return Response({'auth_url': auth_url}, status=status.HTTP_200_OK)

class GitHubCallbackAPIView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            auth = OmniAuthifyDRF(provider_name='github')
            user_info = auth.get_user_info(code)
            print(f"User Info: {user_info}")
            
            # Todo: Authenticate/login the user and save the user_info on your own! or make auto_authenticate True
            return Response({'message': 'User authenticated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ======== Google Login ========
class GoogleLoginAPIView(APIView):
    def get(self, request):
        auth = OmniAuthifyDRF(provider_name='google')
        auth_url = auth.get_auth_url()
        return Response({'auth_url': auth_url}, status=status.HTTP_200_OK)

class GoogleCallbackAPIView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            auth = OmniAuthifyDRF(provider_name='google')
            user_info = auth.get_user_info(code)
            print(f"User Info: {user_info}")
            
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
from .views import (
    FacebookLoginAPIView, FacebookCallbackAPIView,
    GitHubLoginAPIView, GitHubCallbackAPIView,
    GoogleLoginAPIView, GoogleCallbackAPIView,
)

urlpatterns = [
    # ======== Facebook Login ========
    path('facebook/login/', FacebookLoginAPIView.as_view(), name='facebook_login'),
    path('facebook/callback/', FacebookCallbackAPIView.as_view(), name='facebook_callback'),
  
    # ======== GitHub Login ========
    path('github/login/', GitHubLoginAPIView.as_view(), name='github_login'),
    path('github/callback/', GitHubCallbackAPIView.as_view(), name='github_callback'),

    # ======== Google Login ========
    path('google/login/', GoogleLoginAPIView.as_view(), name='google_login'),
    path('google/callback/', GoogleCallbackAPIView.as_view(), name='google_callback'),
  
]
```

---

## ✅ Best Practices

- **🔒 Use Environment Variables**: Always use environment variables to store important information like `client_id` and `client_secret`. This helps keep your credentials safe 🛡️.
- **🔗 Match Redirect URI**: Make sure the `redirect_uri` is consistent between your Provider App settings and your code to avoid errors 🚫.

---

**Omni-Authify** makes adding Provider authentication to your Django REST Framework app straightforward and secure. 
Follow these steps and best practices to provide your users with a seamless login experience. 🚀✨