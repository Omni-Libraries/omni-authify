# Django Integration for Oauth2 authentication

Easily integrate OAuth2 authentication into your Django project using Omni-Authify. This guide covers configuration, view creation, URL setup, and handling user authentication, providing a seamless experience for developers.

---

## ⚙️ Configure Settings

Add the Omni-Authify settings to your Django project settings to include Facebook, GitHub and/or any other OAuth 
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
            'redirect_uri':os.getenv('GITHUB_CLIENT_REDIRECT_URI'),
            'state': os.getenv('GITHUB_STATE'),
            'scope':os.getenv('GITHUB_CLIENT_SCOPE'),
        },
                
        # Add other providers here if needed
        'google': {
            # Coming....
        }
    }
}
```

---

## Django Views

Learn how to create views to handle Facebook,GitHub login and callback in your Django application.

### 📝 Prerequisites

- **Installation**: Install Omni-Authify with Django support using the following command:

  ```bash
  pip install omni-authify[django]
  ```

- **Django 4.2 or higher**
- Omni-Authify installed and configured (see [Installation Guide](../installation.md))

### 🚀 Setting Up Views

Create class based views to handle the login and callback processes.

## 🔁 **views.py**

This version leverages the OmniAuthifyDjango helper class for a simpler implementation over function based views!.

```python
from django.http import HttpResponse
from omni_authify.frameworks.django import OmniAuthifyDjango

# ======== Facebook Login ========
def facebook_login(request):
    auth = OmniAuthifyDjango(provider_name='facebook')
    return auth.login(request)

def facebook_callback(request):
    auth = OmniAuthifyDjango(provider_name='facebook')
    user_info = auth.callback(request)
    print(f"User info from Facebook: {user_info}")
    
     # Todo: Authenticate/login the user and save the user_info on your own!
    return HttpResponse(user_info)

# ======== GitHub Login ========
def github_login(request):
    auth = OmniAuthifyDjango(provider_name='github')
    return auth.login(request)

def github_callback(request)
    auth = OmniAuthifyDjango(provider_name='github')
    user_info = auth.callback(request)
    print(f"User info from Github: {user_info}")

     # Todo: Authenticate/login the user and save the user_info on your own!
    return HttpResponse(user_info)
```

## 🌐 Update URLs

Add the login and callback views to your app's **urls.py** file:

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ======== Facebook Login ========
    path('facebook/login/', views.facebook_login, name='facebook_login'),
    path('facebook/callback/', views.facebook_callback, name='facebook_callback'),

    # ======== GitHub Login ========
    path('github/login/', views.github_login, name='github_login'),
    path('github/callback/', views.github_callback, name='github_callback')
]
```

---

## 📄 Templates

Create a template to display user information or login options.

**home.html**

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
</head>
<body>
    {% if user_info %}
        <h1>Welcome, {{ user_info.name }}!</h1>
        <img src="{{ user_info.picture.data.url }}" alt="Profile Picture">
        <p>Email: {{ user_info.email }}</p>
    {% else %}
        <h1>Welcome to Our Site</h1>
        <p>Please log in using one of the options below:</p>
        <a href="{% url 'facebook_login' %}">Login with Facebook</a><br>
        <a href="{% url 'github_login' %}">Login with GitHub</a>
    {% endif %}
</body>
</html>

```

---

## ✅ Best Practices

- **🔒 Use Environment Variables**: Always use environment variables to store important information like `client_id` and `client_secret`. This helps keep your credentials safe 🛡️.
- **🔗 Match Redirect URI**: Make sure the `redirect_uri` is consistent between your Provider App settings and your code to avoid errors 🚫.
- **⚠️ Error Handling**: Ensure all potential errors are handled to provide a smooth user experience 🐞.

---

**Omni-Authify** makes adding Oauth2 authentication to your Django app straightforward and secure. Follow these steps and best practices to provide your users with a seamless login experience. 🚀✨



